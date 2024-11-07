from django import forms
from blog.models import Post


class PostForm(forms.ModelForm):
    """Form for creating a new post."""
    class Meta:
        model = Post
        fields = ["title", "content", "author", "categories", "image"]
