from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from rest_framework.reverse import reverse_lazy

from blog.forms import PostForm
from blog.models import Post


def post_list_view(request: HttpRequest) -> HttpResponse:
    """List all posts. This is a function-based view."""
    posts = Post.objects.all()
    return render(request, "post_list.html", {"posts": posts})


def post_detail_view(request: HttpRequest, pk: int) -> HttpResponse:
    """Show a single post. This is a function-based view."""
    post = get_object_or_404(Post, pk=pk)
    return render(request, "post_detail.html", {"post": post})


class PostListView(ListView):
    """List all posts. This is a class-based view."""
    model = Post
    template_name = "post_list.html"
    context_object_name = "posts"
    ordering = ["-published_date"]
    paginate_by = 10

    def get_queryset(self) -> QuerySet:
        return Post.objects.all()


class PostDetailView(DetailView):
    """Show a single post. This is a class-based view."""
    model = Post
    template_name = "post_detail.html"
    context_object_name = "post"

    def get_queryset(self) -> QuerySet:
        return Post.objects.all()


class PostCreateView(CreateView):
    """Create a new post. This is a class-based view."""
    model = Post
    form_class = PostForm
    template_name = "post_new.html"
    success_url = reverse_lazy("post_list")
