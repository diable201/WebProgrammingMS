from django.contrib import admin
from tasks.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
    )
    search_fields = ("title", "description")
    ordering = ("title",)
    readonly_fields = ("created_at", "updated_at")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "title",
                    "description",
                )
            },
        ),
        ("Время", {"fields": ("created_at", "updated_at")}),
    )
