from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Контент")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self) -> str:
        return self.title

    def __repr__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ["-timestamp"]


class Comment(models.Model):
    content = models.TextField(verbose_name="Контент")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    post = models.ForeignKey(
        Post, related_name="comments", on_delete=models.CASCADE, verbose_name="Пост"
    )

    def __str__(self) -> str:
        return f"Комментарий от {self.author} на пост {self.post}"

    def __repr__(self) -> str:
        return f"Комментарий от {self.author} на пост {self.post}"

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ["-timestamp"]
