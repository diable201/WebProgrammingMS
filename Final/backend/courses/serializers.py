from rest_framework import serializers

from .models import Course
from categories.models import Category
from categories.serializers import CategorySerializer
from users.serializers import UserSerializer


class CourseSerializer(serializers.ModelSerializer):
    instructor = UserSerializer(read_only=True)
    instructor_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        source="instructor",
        queryset=Course._meta.get_field("instructor").related_model.objects.filter(
            is_instructor=True
        ),
    )
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=Category.objects.all(), source="category"
    )

    class Meta:
        model = Course
        fields = [
            "id",
            "title",
            "description",
            "price",
            "category",
            "category_id",
            "created_at",
            "instructor",
            "instructor_id",
        ]

    def create(self, validated_data):
        if not self.context["request"].user.is_instructor:
            raise serializers.ValidationError("Only instructors can create courses.")

        validated_data["instructor"] = self.context["request"].user
        return super().create(validated_data)

    def update(self, instance: Course, validated_data: dict) -> Course:
        if "instructor" in validated_data:
            instance.instructor = validated_data.pop("instructor")
        if "category" in validated_data:
            instance.category = validated_data.pop("category")
        return super().update(instance, validated_data)
