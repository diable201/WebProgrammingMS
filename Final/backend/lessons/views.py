import sys

from rest_framework.exceptions import ValidationError

sys.path.append("..")

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Lesson
from .serializers import LessonSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from progress.models import UserProgress


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        course_id = self.request.query_params.get('course_id')

        if not course_id:
            raise ValidationError({"detail": "course_id is required."})

        try:
            course_id = int(course_id)
        except ValueError:
            raise ValidationError({"detail": "course_id must be a valid integer."})

        return Lesson.objects.filter(course_id=course_id)


    @action(detail=True, methods=["post"], url_path="complete")
    def complete_lesson(self, request, pk=None):
        user = request.user
        lesson = Lesson.objects.get(pk=pk)

        # Get or create UserProgress for the course
        user_progress, created = UserProgress.objects.get_or_create(
            user=user, course=lesson.course
        )

        # Mark lesson as completed
        if lesson.id not in user_progress.completed_lessons:
            user_progress.completed_lessons.append(lesson.id)
            user_progress.save()

        return Response(
            {"detail": "Lesson marked as completed", "completed_lessons": user_progress.completed_lessons},
            status=status.HTTP_200_OK,
        )