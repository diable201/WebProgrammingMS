from django.db import models

from courses.models import Course


class Quiz(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="quizzes",
        verbose_name="Course",
        help_text="Select the course.",
    )
    title = models.CharField(
        max_length=255,
        unique=True,
        blank=False,
        null=False,
        db_index=True,
        verbose_name="Quiz Title",
    )
    total_marks = models.IntegerField(
        verbose_name="Total Marks", help_text="Enter the total marks."
    )


class QuizQuestion(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="questions")
    question_text = models.TextField(
        verbose_name="Question Text", help_text="Enter the question text."
    )
    option_a = models.CharField(
        max_length=255, verbose_name="Option A", help_text="Enter option A."
    )
    option_b = models.CharField(
        max_length=255, verbose_name="Option B", help_text="Enter option B."
    )
    option_c = models.CharField(
        max_length=255, verbose_name="Option C", help_text="Enter option C."
    )
    option_d = models.CharField(
        max_length=255, verbose_name="Option D", help_text="Enter option D."
    )
    correct_option = models.CharField(
        max_length=1, choices=(("A", "A"), ("B", "B"), ("C", "C"), ("D", "D"))
    )
