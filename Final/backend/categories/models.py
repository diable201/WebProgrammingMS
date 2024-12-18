from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        blank=False,
        null=False,
        db_index=True,
        verbose_name="Category Name",
        help_text="Enter the category name.",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Description",
        help_text="Enter the category description.",
        default="",
        max_length=500,
    )

    def __str__(self) -> str:
        return self.name
