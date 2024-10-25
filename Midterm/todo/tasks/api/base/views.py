from typing import Type

from django.conf import settings
from django.core.cache import cache
from django.db.models import QuerySet
from rest_framework import viewsets, permissions, filters, status
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.request import Request
from drf_spectacular.utils import extend_schema
from django_filters.rest_framework import DjangoFilterBackend
import logging

logger = logging.getLogger(__name__)

from tasks.models import Task
from tasks.api.base.serializers.serializers import TaskSerializer
from accounts.permissions import IsOwner


class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = ["title", "description"]
    ordering_fields = ["due_date", "priority", "created_at"]
    filterset_fields = ["status", "priority"]

    @extend_schema(
        summary="Retrieve all tasks for the current user.",
        description="Retrieve all tasks for the current user.",
    )
    def get_queryset(self) -> QuerySet:
        if not self.request.user.is_authenticated:
            return Task.objects.none()

        cache_key = f"user_tasks_{self.request.user.id}"
        task_ids = cache.get(cache_key)

        if task_ids is None:
            tasks = Task.active_tasks().filter(user=self.request.user)
            task_ids = list(tasks.values_list("id", flat=True))
            cache.set(cache_key, task_ids, timeout=settings.CACHE_TTL)

        return Task.objects.filter(id__in=task_ids)

    def get_object(self) -> Task:
        task_id = self.kwargs.get("pk")
        cache_key = f"user_tasks_{self.request.user.id}_{task_id}"
        task = cache.get(cache_key)

        if task:
            logger.info(f"Cache hit for task {task_id}")
        else:
            logger.info(f"Cache miss for task {task_id}")
            try:
                task = Task.objects.get(id=task_id, is_deleted=False, is_archived=False)
                cache.set(cache_key, task, timeout=settings.CACHE_TTL)
            except Task.DoesNotExist:
                raise NotFound(detail=f"Task with ID {task_id} not found.")

        self.check_object_permissions(self.request, task)
        return task

    def get_serializer_class(self) -> Type[TaskSerializer]:
        return TaskSerializer

    def perform_create(self, serializer: TaskSerializer) -> None:
        serializer.save(user=self.request.user)
        cache.delete(f"user_tasks_{self.request.user.id}")

    def invalidate_task_cache(self, task_id: int) -> None:
        cache.delete(f"user_tasks_{self.request.user.id}_{task_id}")
        cache.delete(f"user_tasks_{self.request.user.id}")
        cache.delete(f"archived_tasks_{self.request.user.id}")

    @action(detail=True, methods=["patch"])
    def archive(self, request: Request, pk: int = None) -> Response:
        task: Task = self.get_object()
        task.archive()
        self.invalidate_task_cache(task.id)
        serializer = self.get_serializer(task)
        return Response(serializer.data)

    @action(detail=True, methods=["patch"])
    def change_status(self, request: Request, pk: int = None) -> Response:
        task_status = request.data.get("status")
        task: Task = self.get_object()
        task.change_status(task_status)
        self.invalidate_task_cache(task.id)
        serializer = self.get_serializer(task)
        return Response(serializer.data)

    @action(detail=True, methods=["patch"])
    def unarchive(self, request: Request, pk: int = None) -> Response:
        task: Task = self.get_object()
        task.unarchive()
        self.invalidate_task_cache(task.id)
        serializer = self.get_serializer(task)
        return Response(serializer.data)

    @action(detail=True, methods=["patch"])
    def change_priority(self, request: Request, pk: int = None) -> Response:
        task: Task = self.get_object()
        priority = request.data.get("priority")

        valid_priorities = dict(Task.PRIORITY_CHOICES).keys()
        if priority not in valid_priorities:
            return Response(
                {"error": "Invalid priority"}, status=status.HTTP_400_BAD_REQUEST
            )

        task.change_priority(priority)
        self.invalidate_task_cache(task.id)

        serializer = self.get_serializer(task)
        return Response(serializer.data)

    @action(detail=True, methods=["patch"])
    def change_due_date(self, request: Request, pk: int = None) -> Response:
        task: Task = self.get_object()
        due_date = request.data.get("due_date")

        try:
            task.change_due_date(due_date)
        except ValueError:
            return Response(
                {"error": "Invalid date format"}, status=status.HTTP_400_BAD_REQUEST
            )

        self.invalidate_task_cache(task.id)

        serializer = self.get_serializer(task)
        return Response(serializer.data)

    @action(detail=True, methods=["delete"])
    def soft_delete(self, request: Request, pk: int = None) -> Response:
        task: Task = self.get_object()
        task.soft_delete()

        self.invalidate_task_cache(task.id)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=["get"])
    def archived(self, request: Request) -> Response:
        cache_key = f"archived_tasks_{request.user.id}"
        tasks = cache.get(cache_key)

        if tasks is None:
            tasks = Task.archived_tasks().filter(user=request.user)
            cache.set(cache_key, list(tasks), timeout=settings.CACHE_TTL)
        else:
            task_ids = [task.id for task in tasks]
            tasks = Task.objects.filter(id__in=task_ids)

        serializer = self.get_serializer(tasks, many=True)
        return Response(serializer.data)

    def perform_update(self, serializer):
        task = serializer.instance
        self.invalidate_task_cache(task.id)
        return super().perform_update(serializer)

    def partial_update(self, request, *args, **kwargs):
        self.invalidate_task_cache(kwargs["pk"])
        return super().partial_update(request, *args, **kwargs)
