from rest_framework import serializers
from .models import Lesson


class LessonSerializer(serializers.ModelSerializer):
    course_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        source="course",
        queryset=Lesson._meta.get_field("course").related_model.objects.all(),
    )

    class Meta:
        model = Lesson
        fields = ["id", "course_id", "title", "content", "video_url"]
