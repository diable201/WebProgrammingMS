from drf_spectacular.utils import extend_schema, OpenApiExample
from rest_framework import viewsets, permissions, status
from rest_framework.request import Request
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer, UserRegisterSerializer
from rest_framework.decorators import action


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("id")
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action == "create":
            return UserRegisterSerializer
        return UserSerializer

    @extend_schema(
        request=UserRegisterSerializer,
        responses={201: UserSerializer},
        examples=[
            OpenApiExample(
                "Register Example",
                description="Example of user registration payload",
                value={
                    "username": "john_doe",
                    "email": "john@example.com",
                    "password": "SecurePassword123",
                    "password_confirmation": "SecurePassword123",
                    "is_student": True,
                    "is_instructor": False,
                },
            )
        ],
    )
    @action(detail=False, methods=["post"], permission_classes=[permissions.AllowAny])
    def register(self, request: Request) -> Response:
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)

    @action(
        detail=False, methods=["get"], permission_classes=[permissions.IsAuthenticated]
    )
    def me(self, request: Request) -> Response:
        return Response(UserSerializer(request.user).data)

    @action(
        detail=False,
        methods=["patch"],
        permission_classes=[permissions.IsAuthenticated],
    )
    def update_me(self, request: Request) -> Response:
        serializer = UserSerializer(request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(UserSerializer(user).data)

    @action(
        detail=False,
        methods=["delete"],
        permission_classes=[permissions.IsAuthenticated],
    )
    def delete_me(self, request: Request) -> Response:
        request.user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def create(self, request: Request, *args, **kwargs) -> Response:
        return Response(
            status=status.HTTP_405_METHOD_NOT_ALLOWED,
            data={"detail": "Method Not Allowed"},
        )
