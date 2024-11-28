from rest_framework import serializers

from blog.models import Comment, Post


class CommentSerializerV1(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Comment
        fields = ["id", "content", "author_username", "timestamp", "post"]
        extra_kwargs = {"author": {"read_only": True}}


class PostSerializerV1(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source="author.username")
    comments = CommentSerializerV1(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ["id", "title", "content", "author_username", "timestamp", "comments"]
        extra_kwargs = {"author": {"read_only": True}}
