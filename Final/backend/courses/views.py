from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from rest_framework import viewsets

from .forms import CourseForm
from .models import Course
from .serializers import CourseSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

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

    def get_permissions(self):
        if self.action in ['create', 'update', 'delete']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/course_detail.html'
    context_object_name = 'course'


def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'courses/create_course.html', {'form': form})


def api_course_list(request):
    courses = Course.objects.values('id', 'title', 'description', 'price')
    return JsonResponse({'courses': list(courses)})
