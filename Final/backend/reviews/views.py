from rest_framework import viewsets, permissions
from .models import Review
from .serializers import ReviewSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all().order_by("-created_at")
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        """
        Optionally filter reviews by 'course_id' query parameter.
        """
        queryset = self.queryset
        course_id = self.request.query_params.get('course_id')
        if course_id:
            queryset = queryset.filter(course_id=course_id)
        return queryset

    def perform_create(self, serializer):
        """
        Automatically set the 'user' field to the currently authenticated user.
        """
        serializer.save(user=self.request.user)
