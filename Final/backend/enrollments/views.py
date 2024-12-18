from rest_framework import viewsets
from .models import Enrollment
from .serializers import EnrollmentSerializer


class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        course_id = self.request.query_params.get('course_id')
        queryset = self.queryset

        if user_id:
            queryset = queryset.filter(user_id=user_id)
        if course_id:
            queryset = queryset.filter(course_id=course_id)

        return queryset
