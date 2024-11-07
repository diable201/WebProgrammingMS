# Generated by Django 5.1.2 on 2024-11-06 14:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        help_text="Максимум 100 символов",
                        max_length=100,
                        verbose_name="Название",
                    ),
                ),
                (
                    "content",
                    models.TextField(
                        blank=True, help_text="Текст статьи", verbose_name="Контент"
                    ),
                ),
                (
                    "published_date",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="Дата публикации статьи",
                        verbose_name="Дата публикации",
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        help_text="Автор статьи",
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Автор",
                    ),
                ),
            ],
            options={
                "verbose_name": "Статья",
                "verbose_name_plural": "Статьи",
                "ordering": ("-published_date",),
            },
        ),
    ]
