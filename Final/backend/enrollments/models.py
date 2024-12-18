from django.db import models
from django.conf import settings

from courses.models import Course


class Enrollment(models.Model):
    STATUS_CHOICES = (
        ("active", "Active"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="enrollments",
        verbose_name="User",
        help_text="Select the user.",
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="enrollments",
        verbose_name="Course",
        help_text="Select the course.",
    )
    enrollment_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Enrollment Date",
        help_text="The date and time this course was enrolled.",
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="active",
        verbose_name="Status",
        help_text="Select the enrollment status.",
    )

    def __str__(self) -> str:
        return f"{self.user.username} enrolled in {self.course.title}"
