from rest_framework import serializers
from .models import Quiz, QuizQuestion


class QuizQuestionSerializer(serializers.ModelSerializer):
    options = serializers.SerializerMethodField()

    class Meta:
        model = QuizQuestion
        fields = ["id", "question_text", "options"]

    def get_options(self, obj):
        """
        Return options as a list of dictionaries for clean rendering.
        """
        return [
            {"id": "A", "text": obj.option_a},
            {"id": "B", "text": obj.option_b},
            {"id": "C", "text": obj.option_c},
            {"id": "D", "text": obj.option_d},
        ]



class QuizSerializer(serializers.ModelSerializer):
    questions = QuizQuestionSerializer(source="questions.all", many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = ["id", "title", "course", "total_marks", "questions"]

