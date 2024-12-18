from rest_framework import viewsets, permissions
from .models import UserProgress
from .serializers import UserProgressSerializer


class UserProgressViewSet(viewsets.ModelViewSet):
    queryset = UserProgress.objects.all()
    serializer_class = UserProgressSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        course_id = self.request.query_params.get('course_id')
        queryset = UserProgress.objects.filter(user=user)
        if course_id:
            queryset = queryset.filter(course_id=course_id)
        return queryset

    def perform_create(self, serializer):
        if "user" not in serializer.validated_data:
            serializer.save(user=self.request.user)
        else:
            serializer.save()
