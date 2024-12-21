from .models import Course
from django import forms


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'price', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Course Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Course Description'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Course Price'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Course Title',
            'description': 'Course Description',
            'price': 'Price (USD)',
            'category': 'Category',
        }
