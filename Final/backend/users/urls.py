from django.urls import path
from .views import UserViewSet

urlpatterns = [
    path("register/", UserViewSet.as_view({"post": "create"}), name="register"),
    path(
        "me/",
        UserViewSet.as_view({"get": "me", "patch": "update_me", "delete": "delete_me"}),
        name="me",
    ),
]
