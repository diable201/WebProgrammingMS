from rest_framework import serializers
from .models import Enrollment


class EnrollmentSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        source="user",
        queryset=Enrollment._meta.get_field("user").related_model.objects.all(),
    )
    course_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        source="course",
        queryset=Enrollment._meta.get_field("course").related_model.objects.all(),
    )

    class Meta:
        model = Enrollment
        fields = ["id", "user_id", "course_id", "enrollment_date", "status"]

    def create(self, validated_data: dict) -> Enrollment:
        return super().create(validated_data)
