from rest_framework import serializers

from blog.models import Comment, Post


class CommentSerializerV2(serializers.ModelSerializer):
    author_full_name = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ["id", "content", "author_full_name", "timestamp"]

    @staticmethod
    def get_author_full_name(obj: Comment) -> str:
        return f"{obj.author.first_name} {obj.author.last_name}"


class PostSerializerV2(serializers.ModelSerializer):
    author_full_name = serializers.SerializerMethodField()
    comments = CommentSerializerV2(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ["id", "title", "content", "author_full_name", "timestamp", "comments"]

    @staticmethod
    def get_author_full_name(obj: Post) -> str:
        return f"{obj.author.first_name} {obj.author.last_name}"
