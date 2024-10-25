from django.contrib import admin
from accounts.models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "bio", "location")
    search_fields = ("user__username", "bio", "location")
    list_filter = ("location",)
    ordering = ("user",)
    readonly_fields = ("user", "get_full_name")
    fieldsets = (
        (None, {"fields": ("user",)}),
        ("Дополнительная информация", {"fields": ("bio", "location",)}),
    )
