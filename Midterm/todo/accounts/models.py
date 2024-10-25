from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile",
        verbose_name=_("Пользователь"),
    )
    bio = models.TextField(blank=True, null=True, verbose_name=_("О себе"))
    location = models.CharField(
        max_length=255, blank=True, null=True, verbose_name=_("Местоположение")
    )

    def __str__(self) -> str:
        return self.user.username

    def __repr__(self) -> str:
        return f"UserProfile(user={self.user.username})"

    def get_full_name(self) -> str:
        return f"{self.user.first_name} {self.user.last_name}"

    class Meta:
        verbose_name = _("Профиль пользователя")
        verbose_name_plural = _("Профили пользователей")
        indexes = [models.Index(fields=["user"])]
        ordering = ["user"]
