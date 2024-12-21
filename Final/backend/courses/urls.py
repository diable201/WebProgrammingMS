from django.urls import path
from .views import course_list, CourseDetailView, create_course

urlpatterns = [
    path('', course_list, name='course_list'),
    path('course/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('course/create/', create_course, name='create_course'),
]
