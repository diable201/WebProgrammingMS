from django.urls import include, path
from rest_framework.authtoken import views as drf_views
from rest_framework.routers import DefaultRouter

from blog.api.views_v2 import CommentViewSetV2, PostViewSetV2

router = DefaultRouter()
router.register(r"posts", PostViewSetV2, basename="post")

urlpatterns = [
    path("", include(router.urls)),
    path(
        "posts/<int:post_pk>/comments/",
        CommentViewSetV2.as_view({"get": "list", "post": "create"}),
        name="post-comments",
    ),
    path(
        "posts/<int:post_pk>/comments/<int:pk>/",
        CommentViewSetV2.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="post-comment-detail",
    ),
    path("api-token-auth/", drf_views.obtain_auth_token, name="api-token-auth"),
]
