from rest_framework import serializers
from .models import Category, Tag, Author, Post


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "description"]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name", "slug"]


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "bio",
            "website",
            "date_joined",
            "last_login",
        ]
        read_only_fields = ["username", "email", "date_joined", "last_login"]


class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    categories = CategorySerializer(many=True, required=False)
    tags = TagSerializer(many=True, required=False)

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "author",
            "content",
            "published_at",
            "created_at",
            "updated_at",
            "status",
            "categories",
            "tags",
        ]
        read_only_fields = ["id", "author", "published_at", "created_at", "updated_at"]

    def create(self, validated_data):
        categories_data = validated_data.pop("categories", [])
        tags_data = validated_data.pop("tags", [])
        post = Post.objects.create(
            author=self.context["request"].user, **validated_data
        )

        for category_data in categories_data:
            category, created = Category.objects.get_or_create(**category_data)
            post.categories.add(category)

        for tag_data in tags_data:
            tag, created = Tag.objects.get_or_create(**tag_data)
            post.tags.add(tag)

        return post

    def update(self, instance, validated_data):
        categories_data = validated_data.pop("categories", [])
        tags_data = validated_data.pop("tags", [])

        instance = super().update(instance, validated_data)

        if categories_data:
            instance.categories.clear()
            for category_data in categories_data:
                category, created = Category.objects.get_or_create(**category_data)
                instance.categories.add(category)

        if tags_data:
            instance.tags.clear()
            for tag_data in tags_data:
                tag, created = Tag.objects.get_or_create(**tag_data)
                instance.tags.add(tag)

        return instance
