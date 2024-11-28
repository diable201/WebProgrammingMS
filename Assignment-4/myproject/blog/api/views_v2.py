from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import permissions, viewsets

from blog.api.base.serializers.serializers_v2 import (
    CommentSerializerV2,
    PostSerializerV2,
)
from blog.api.base_views import BaseCommentViewSet
from blog.models import Post
from blog.permissions import IsAuthorOrReadOnly


@extend_schema_view(
    list=extend_schema(description="Retrieve a list of posts (v2)."),
    retrieve=extend_schema(description="Retrieve a single post (v2)."),
    create=extend_schema(description="Create a new post (v2)."),
    update=extend_schema(description="Update an existing post (v2)."),
    destroy=extend_schema(description="Delete a post (v2)."),
)
class PostViewSetV2(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-timestamp")
    serializer_class = PostSerializerV2
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


@extend_schema_view(
    list=extend_schema(description="List comments for a post (v2)."),
    retrieve=extend_schema(description="Retrieve a single comment (v2)."),
    create=extend_schema(description="Create a new comment for a post (v2)."),
    update=extend_schema(description="Update a comment (v2)."),
    destroy=extend_schema(description="Delete a comment (v2)."),
)
class CommentViewSetV2(BaseCommentViewSet):
    serializer_class = CommentSerializerV2
