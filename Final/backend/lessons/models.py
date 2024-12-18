from django.db import models

from courses.models import Course


class Lesson(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="lessons",
        verbose_name="Course",
        help_text="Select the course.",
    )
    title = models.CharField(
        max_length=255,
        unique=True,
        blank=False,
        null=False,
        db_index=True,
        verbose_name="Lesson Title",
    )
    content = models.TextField(
        verbose_name="Content",
        help_text="Enter the lesson content.",
        default="",
        blank=True,
        null=True,
    )
    video_url = models.URLField(
        blank=True,
        null=True,
        verbose_name="Video URL",
        help_text="Enter the video URL.",
    )

    def __str__(self) -> str:
        return f"{self.title} - {self.course.title}"
