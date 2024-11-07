from django.urls import path

from blog.api.base.views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    post_list_view,
    post_detail_view,
)

urlpatterns = [
    path("posts/", PostListView.as_view(), name="post_list"),
    path("posts/new/", PostCreateView.as_view(), name="post_new"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
]
