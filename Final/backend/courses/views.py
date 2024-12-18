from rest_framework import viewsets

from .models import Course
from .serializers import CourseSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from users.models import User


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all().order_by("-created_at")
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer: CourseSerializer) -> None:
        user = self.request.user
        if not user.is_instructor:
            raise PermissionError("Only instructors can create courses.")
        serializer.save(instructor=user)
