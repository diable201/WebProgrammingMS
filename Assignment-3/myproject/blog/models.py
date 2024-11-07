from django.db import models
from django.contrib.auth.models import User

from blog.manager import PostManager


class Category(models.Model):
    name = models.CharField(
        max_length=50, verbose_name="Название", help_text="Максимум 50 символов"
    )
    description = models.TextField(
        blank=True, verbose_name="Описание", help_text="Описание категории"
    )

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"Category(name={self.name})"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ("name",)


class Post(models.Model):
    title = models.CharField(
        max_length=100, verbose_name="Название", help_text="Максимум 100 символов"
    )
    content = models.TextField(
        blank=True, verbose_name="Контент", help_text="Текст статьи"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Автор", help_text="Автор статьи"
    )
    published_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата публикации",
        help_text="Дата публикации статьи",
    )
    categories = models.ManyToManyField(
        Category, verbose_name="Категории", help_text="Категории статьи"
    )
    image = models.ImageField(
        upload_to="post_images/", null=True, blank=True, verbose_name="Изображение"
    )
    objects = PostManager()

    def __str__(self) -> str:
        return self.title

    def __repr__(self) -> str:
        return f"Post(title={self.title}, author={self.author}, published_date={self.published_date})"

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ("-published_date",)


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name="Статья",
        help_text="Статья к которой относится комментарий",
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Автор",
        help_text="Автор комментария",
    )
    content = models.TextField(verbose_name="Контент", help_text="Текст комментария")
    published_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата публикации",
        help_text="Дата публикации комментария",
    )

    def __str__(self) -> str:
        return f"{self.author} - {self.published_date}"

    def __repr__(self) -> str:
        return f"Comment(author={self.author}, published_date={self.published_date})"

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ("-published_date",)
