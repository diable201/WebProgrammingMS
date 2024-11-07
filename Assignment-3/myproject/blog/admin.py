from django.contrib import admin
from blog.models import Post, Category, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Admin panel configuration for the Post model."""
    list_display = ("title", "author", "published_date")
    list_filter = ("author", "published_date")
    search_fields = ("title", "content")
    ordering = ("-published_date",)
    fields = ("title", "content", "author", "published_date")
    readonly_fields = ("published_date",)
    list_per_page = 10


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Admin panel configuration for the Category model."""
    list_display = ("name", "description")
    search_fields = ("name",)
    ordering = ("name",)
    list_per_page = 10


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Admin panel configuration for the Comment model."""
    list_display = ("post", "author")
    list_filter = ("author",)
    search_fields = ("post__title", "content")
    ordering = ("-published_date",)
    fields = ("post", "author", "content", "published_date")
    readonly_fields = ("published_date",)
    list_per_page = 10
