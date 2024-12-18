from drf_spectacular.utils import extend_schema, OpenApiExample
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import Quiz, QuizQuestion
from .serializers import QuizSerializer, QuizQuestionSerializer
from progress.models import UserProgress


class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        """
        Optionally filter quizzes by course ID.
        """
        course_id = self.request.query_params.get('course_id')
        if course_id:
            return self.queryset.filter(course_id=course_id)
        return self.queryset


class QuizQuestionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = QuizQuestion.objects.all()
    serializer_class = QuizQuestionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        """
        Filter questions by quiz ID if provided in the query parameters.
        """
        quiz_id = self.request.query_params.get("quiz_id")
        if quiz_id:
            return self.queryset.filter(quiz__id=quiz_id)
        return self.queryset


class QuizSubmissionView(RetrieveModelMixin, GenericViewSet):
    queryset = Quiz.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = QuizSerializer

    @extend_schema(
        request={
            "application/json": {
                "example": {
                    "answers": {
                        "1": "A",
                        "2": "B",
                        "3": "D"
                    }
                }
            }
        },
        responses={
            200: OpenApiExample(
                name="Successful Submission",
                value={
                    "detail": "Quiz submitted",
                    "score": 85
                },
                response_only=True
            )
        },
        description="Submit a quiz with answers for the given quiz ID."
    )
    @action(detail=True, methods=["post"])
    def submit(self, request, pk=None):
        """
        Handle quiz submission, calculate scores, and update user progress.
        """
        quiz = self.get_object()
        answers = request.data.get("answers", {})

        # Validate user's enrollment in quiz.course
        total_questions = quiz.questions.count()
        correct_count = 0
        for q in quiz.questions.all():
            print("DSLAKDLKSALD:")
            print(q.correct_option)
            user_answer = answers.get(str(q.id))
            print(user_answer)
            if user_answer and user_answer == q.correct_option:
                print("Correct")
                correct_count += 1

        score = int((correct_count / total_questions) * quiz.total_marks)

        # Update UserProgress
        user_progress, created = UserProgress.objects.get_or_create(
            user=request.user,
            course=quiz.course,
        )

        if quiz.id not in user_progress.completed_lessons:
            user_progress.completed_lessons.append(quiz.id)
        user_progress.quiz_scores[str(quiz.id)] = score
        user_progress.save()

        return Response(
            {"detail": "Quiz submitted", "score": score}, status=status.HTTP_200_OK
        )
