from django.db import models
from django.conf import settings

from categories.models import Category


class Course(models.Model):
    title = models.CharField(
        max_length=255,
        unique=True,
        blank=False,
        null=False,
        db_index=True,
        verbose_name="Course Title",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Description",
        help_text="Enter the course description.",
        default="",
        max_length=500,
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Price",
        help_text="Enter the course price.",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name="courses",
        verbose_name="Category",
        help_text="Select the course category.",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At",
        help_text="The date and time this course was created.",
    )
    instructor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="courses",
        verbose_name="Instructor",
        help_text="Select the course instructor.",
    )

    def __str__(self) -> str:
        return self.title
