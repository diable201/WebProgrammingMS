"""
URL configuration for elearning project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from courses.views import CourseViewSet
from enrollments.views import EnrollmentViewSet
from lessons.views import LessonViewSet
from reviews.views import ReviewViewSet
from categories.views import CategoryViewSet
from payments.views import PaymentViewSet
from quizzes.views import QuizViewSet, QuizQuestionViewSet, QuizSubmissionView
from progress.views import UserProgressViewSet
from users.views import UserViewSet

router = routers.DefaultRouter()
router.register(r"users", UserViewSet, basename="users")
router.register(r"courses", CourseViewSet, basename="courses")
router.register(r"enrollments", EnrollmentViewSet, basename="enrollments")
router.register(r"lessons", LessonViewSet, basename="lessons")
router.register(r"reviews", ReviewViewSet, basename="reviews")
router.register(r"categories", CategoryViewSet, basename="categories")
router.register(r"payments", PaymentViewSet, basename="payments")
router.register(r"quizzes", QuizViewSet, basename="quizzes")
router.register(r"quiz-questions", QuizQuestionViewSet, basename="quizquestions")
router.register(r"progress", UserProgressViewSet, basename="progress")
router.register(r"quiz-submission", QuizSubmissionView, basename="quiz-submission")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/token/", TokenObtainPairView.as_view(), name="token_obtain"),
    path("api/auth/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/", include(router.urls)),
    path("api/users/", include("users.urls")),
    path("api/templates/", include("courses.urls")),
]

if settings.DEBUG:
    from drf_spectacular.views import (
        SpectacularAPIView,
        SpectacularRedocView,
        SpectacularSwaggerView,
    )

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += [
        path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
        path(
            "api/schema/swagger-ui/",
            SpectacularSwaggerView.as_view(url_name="schema"),
            name="swagger-ui",
        ),
        path(
            "api/schema/redoc/",
            SpectacularRedocView.as_view(url_name="schema"),
            name="redoc",
        ),
    ]
