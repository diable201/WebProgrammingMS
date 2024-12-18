from django.db import models
from django.conf import settings

from courses.models import Course


class Review(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="reviews",
        verbose_name="Course",
        help_text="Select the course.",
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="reviews",
        verbose_name="User",
        help_text="Select the user.",
    )
    rating = models.IntegerField(verbose_name="Rating", help_text="Enter the rating.")
    comment = models.TextField(
        verbose_name="Comment",
        help_text="Enter the comment.",
        default="",
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At",
        help_text="The date and time this review was created.",
    )
