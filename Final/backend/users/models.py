from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_student = models.BooleanField(
        default=False,
        help_text="Designates whether this user should be treated as a student.",
        verbose_name="student status",
    )
    is_instructor = models.BooleanField(
        default=False,
        help_text="Designates whether this user should be treated as an instructor.",
        verbose_name="instructor status",
    )

    def __str__(self) -> str:
        return self.username

    def __repr__(self) -> str:
        return self.username

