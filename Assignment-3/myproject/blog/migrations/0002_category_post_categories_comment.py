# Generated by Django 5.1.2 on 2024-11-06 14:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                    "name",
                    models.CharField(
                        help_text="Максимум 50 символов",
                        max_length=50,
                        verbose_name="Название",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="Описание категории",
                        verbose_name="Описание",
                    ),
                ),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
                "ordering": ("name",),
            },
        ),
        migrations.AddField(
            model_name="post",
            name="categories",
            field=models.ManyToManyField(
                help_text="Категории статьи",
                to="blog.category",
                verbose_name="Категории",
            ),
        ),
        migrations.CreateModel(
            name="Comment",
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
                    "content",
                    models.TextField(
                        help_text="Текст комментария", verbose_name="Контент"
                    ),
                ),
                (
                    "published_date",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="Дата публикации комментария",
                        verbose_name="Дата публикации",
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        help_text="Автор комментария",
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Автор",
                    ),
                ),
                (
                    "post",
                    models.ForeignKey(
                        help_text="Статья к которой относится комментарий",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="blog.post",
                        verbose_name="Статья",
                    ),
                ),
            ],
            options={
                "verbose_name": "Комментарий",
                "verbose_name_plural": "Комментарии",
                "ordering": ("-published_date",),
            },
        ),
    ]
