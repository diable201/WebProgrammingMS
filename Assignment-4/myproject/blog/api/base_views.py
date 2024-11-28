from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from rest_framework import permissions, viewsets

from blog.models import Comment
from blog.permissions import IsAuthorOrReadOnly


class BaseCommentViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def get_queryset(self):
        return Comment.objects.filter(post=self.kwargs["post_pk"]).order_by(
            "-timestamp"
        )

    def perform_create(self, serializer):
        comment = serializer.save(
            author=self.request.user, post_id=self.kwargs["post_pk"]
        )
        channel_layer = get_channel_layer()
        group_name = f"user_{comment.post.author.id}"
        message = {
            "message": f'New comment on your post "{comment.post.title}": {comment.content}',
            "post_id": comment.post.id,
            "comment_id": comment.id,
        }
        async_to_sync(channel_layer.group_send)(
            group_name,
            {
                "type": "send_notification",
                "message": message,
            },
        )
