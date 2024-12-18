from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    course_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        source="course",
        queryset=Review._meta.get_field("course").related_model.objects.all(),
    )

    class Meta:
        model = Review
        fields = ["id", "course_id", "user", "rating", "comment", "created_at"]
        read_only_fields = ["user", "created_at"]

    def create(self, validated_data: dict) -> Review:
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)
