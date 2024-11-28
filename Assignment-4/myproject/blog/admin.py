from django.contrib import admin

from blog.models import Comment, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "timestamp"]
    search_fields = ["title", "content"]
    list_filter = ["author", "timestamp"]
    date_hierarchy = "timestamp"
    ordering = ["-timestamp"]
    readonly_fields = ["timestamp"]
    fieldsets = ((None, {"fields": ("title", "content", "author")}),)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["author", "timestamp"]
    search_fields = ["content"]
    list_filter = ["author", "timestamp"]
    date_hierarchy = "timestamp"
    ordering = ["-timestamp"]
    readonly_fields = ["timestamp"]
    fieldsets = ((None, {"fields": ("content", "author", "post")}),)
