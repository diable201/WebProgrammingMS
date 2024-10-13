from django.contrib import admin
from .models import Post, Tag, Category, Author


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "status", "published_at")
    list_filter = ("status", "author", "categories", "tags")
    search_fields = ("title", "content")
    date_hierarchy = "published_at"
    ordering = ("status", "published_at")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description")


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email")
    search_fields = ("first_name", "last_name", "email")
    date_hierarchy = "date_joined"
    ordering = ("last_name", "first_name")
