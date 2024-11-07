from django.db import models
from django.db.models import QuerySet


class PostManager(models.Manager):
    def published(self) -> QuerySet:
        """Return all published posts."""
        return self.filter(published_date__isnull=False)

    def by_author(self, author_username: str) -> QuerySet:
        """Return all posts by the given author."""
        return self.filter(author__username=author_username)
