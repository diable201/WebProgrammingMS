from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import permissions, viewsets

from blog.api.base.serializers.serializers_v1 import (
    CommentSerializerV1,
    PostSerializerV1,
)
from blog.api.base_views import BaseCommentViewSet
from blog.models import Post
from blog.permissions import IsAuthorOrReadOnly


@extend_schema_view(
    list=extend_schema(description="Retrieve a list of posts (v1)."),
    retrieve=extend_schema(description="Retrieve a single post (v1)."),
    create=extend_schema(description="Create a new post (v1)."),
    update=extend_schema(description="Update an existing post (v1)."),
    destroy=extend_schema(description="Delete a post (v1)."),
)
class PostViewSetV1(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-timestamp")
    serializer_class = PostSerializerV1
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


@extend_schema_view(
    list=extend_schema(description="List comments for a post (v1)."),
    retrieve=extend_schema(description="Retrieve a single comment (v1)."),
    create=extend_schema(description="Create a new comment for a post (v1)."),
    update=extend_schema(description="Update a comment (v1)."),
    destroy=extend_schema(description="Delete a comment (v1)."),
)
class CommentViewSetV1(BaseCommentViewSet):
    serializer_class = CommentSerializerV1
