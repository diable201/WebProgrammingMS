from django.db.models import QuerySet

from mixins.models import TimestampMixin

from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Task(TimestampMixin):
    STATUS_CHOICES = [
        ("PENDING", "Ожидает"),
        ("IN_PROGRESS", "В процессе"),
        ("COMPLETED", "Завершено"),
        ("ARCHIVED", "В архиве"),
    ]

    PRIORITY_CHOICES = [
        ("LOW", "Низкий"),
        ("MEDIUM", "Средний"),
        ("HIGH", "Высокий"),
        ("CRITICAL", "Критический"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="tasks",
        verbose_name=_("Пользователь"),
    )
    title = models.CharField(
        max_length=255, verbose_name=_("Имя задачи"), db_index=True
    )
    description = models.TextField(blank=True, null=True, verbose_name=_("Описание"))
    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default="PENDING",
        verbose_name=_("Статус"),
        db_index=True,
    )
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default="MEDIUM",
        verbose_name=_("Приоритет"),
        db_index=True,
    )
    due_date = models.DateTimeField(
        null=True, blank=True, verbose_name=_("Срок выполнения")
    )
    is_archived = models.BooleanField(default=False, verbose_name=_("В архиве?"))
    is_deleted = models.BooleanField(default=False, verbose_name=_("Удалено?"))

    class Meta:
        ordering = ["-created_at"]
        verbose_name = _("Задача")
        verbose_name_plural = _("Задачи")
        indexes = [
            models.Index(fields=["user", "status"]),
        ]

    def __str__(self) -> str:
        return self.title

    def __repr__(self) -> str:
        return f"<Task: {self.title}>"

    def change_priority(self, priority: str) -> None:
        if priority not in dict(self.PRIORITY_CHOICES).keys():
            raise ValueError("Invalid priority value")
        self.priority = priority
        self.save()

    def change_status(self, status: str) -> None:
        if status not in dict(self.STATUS_CHOICES).keys():
            raise ValueError("Invalid status value")
        self.status = status
        self.save()

    def archive(self) -> None:
        self.change_status("ARCHIVED")
        self.is_archived = True
        self.save()

    def unarchive(self) -> None:
        self.change_status("PENDING")
        self.is_archived = False
        self.save()

    def soft_delete(self) -> None:
        self.is_deleted = True
        self.save()

    def is_overdue(self) -> bool:
        return self.due_date and self.due_date < timezone.now()

    def change_due_date(self, due_date: timezone) -> None:
        self.due_date = due_date
        self.save()

    @classmethod
    def active_tasks(cls) -> QuerySet:
        return cls.objects.filter(is_deleted=False, is_archived=False)

    @classmethod
    def archived_tasks(cls) -> QuerySet:
        return cls.objects.filter(is_deleted=False, is_archived=True)
