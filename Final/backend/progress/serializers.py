from rest_framework import serializers
from .models import UserProgress


class UserProgressSerializer(serializers.ModelSerializer):
    course_title = serializers.CharField(source='course.title', read_only=True)
    lessons_completed = serializers.SerializerMethodField()
    total_lessons = serializers.SerializerMethodField()
    quizzes_completed = serializers.SerializerMethodField()
    total_quizzes = serializers.SerializerMethodField()

    class Meta:
        model = UserProgress
        fields = [
            'id',
            'course_title',
            'lessons_completed',
            'total_lessons',
            'quizzes_completed',
            'total_quizzes',
            'completed_lessons',
        ]

    def get_lessons_completed(self, obj):
        return len(obj.completed_lessons) if obj.completed_lessons else 0

    def get_total_lessons(self, obj):
        return obj.course.lessons.count() if obj.course else 0

    def get_quizzes_completed(self, obj):
        return len(obj.quiz_scores) if obj.quiz_scores else 0

    def get_total_quizzes(self, obj):
        return obj.course.quizzes.count() if obj.course else 0
