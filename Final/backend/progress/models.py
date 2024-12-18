from django.db import models
from django.conf import settings

from courses.models import Course


class UserProgress(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="progress",
        verbose_name="User",
        help_text="Select the user.",
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="progress",
        verbose_name="Course",
        help_text="Select the course.",
    )
    completed_lessons = models.JSONField(
        default=list,
        verbose_name="Completed Lessons",
        blank=True,
        null=True,
    )
    quiz_scores = models.JSONField(
        default=dict,
        verbose_name="Quiz Scores",
        help_text="Enter the quiz scores.",
        blank=True,
        null=True,
    )
