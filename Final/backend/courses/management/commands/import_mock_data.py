import json
from django.core.management.base import BaseCommand
from courses.models import Course
from categories.models import Category
from lessons.models import Lesson
from quizzes.models import Quiz, QuizQuestion

class Command(BaseCommand):
    help = 'Load mock data into the database'

    def handle(self, *args, **kwargs):
        with open('courses/management/commands/categories.json', 'r') as file:
            categories = json.load(file)
            for category in categories:
                Category.objects.get_or_create(
                    id=category['id'],
                    name=category['name'],
                    description=category['description']
                )
        self.stdout.write(self.style.SUCCESS('Categories loaded successfully!'))

        with open('courses/management/commands/courses.json', 'r') as file:
            courses = json.load(file)
            for course in courses:
                Course.objects.get_or_create(
                    id=course['course_id'],
                    title=course['title'],
                    description=course['description'],
                    price=course['price'],
                    category_id=course['category_id'],
                    created_at=course['created_at'],
                    instructor_id=course['instructor_id'],
                    image=course['image']
                )
        self.stdout.write(self.style.SUCCESS('Courses loaded successfully!'))

        with open('courses/management/commands/lessons.json', 'r') as file:
            lessons = json.load(file)
            for lesson in lessons:
                Lesson.objects.get_or_create(
                    id=lesson['lesson_id'],
                    course_id=lesson['course_id'],
                    title=lesson['title'],
                    content=lesson['content'],
                    video_url=lesson['video_url']
                )
        self.stdout.write(self.style.SUCCESS('Lessons loaded successfully!'))

        with open('courses/management/commands/quizzes.json', 'r') as file:
            quizzes = json.load(file)
            for quiz in quizzes:
                quiz_obj, created = Quiz.objects.get_or_create(
                    id=quiz['quiz_id'],
                    course_id=quiz['course_id'],
                    title=quiz['title'],
                    total_marks=quiz['total_marks']
                )
                for question in quiz['questions']:
                    QuizQuestion.objects.get_or_create(
                        id=question['question_id'],
                        quiz=quiz_obj,
                        question_text=question['question_text'],
                        option_a=question['option_a'],
                        option_b=question['option_b'],
                        option_c=question['option_c'],
                        option_d=question['option_d'],
                        correct_option=question['correct_option']
                    )
        self.stdout.write(self.style.SUCCESS('Quizzes and Questions loaded successfully!'))
