from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile
from typing import Any


@receiver(post_save, sender=User)
def create_or_update_user_profile(
    sender: User, instance: User, created: bool, **kwargs: dict[str, Any]
) -> None:
    if created:
        UserProfile.objects.create(user=instance)
    instance.profile.save()
