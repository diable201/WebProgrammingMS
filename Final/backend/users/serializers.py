from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "is_student", "is_instructor"]


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password_confirmation = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password",
            "password_confirmation",
            "is_student",
            "is_instructor",
        ]

    def validate(self, attrs: dict) -> dict:
        if attrs["password"] != attrs["password_confirmation"]:
            raise serializers.ValidationError({"password": "Passwords didn't match."})
        return attrs

    @staticmethod
    def validate_username(value: str) -> str:
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username is already taken.")
        return value

    def create(self, validated_data: dict) -> User:
        validated_data.pop("password_confirmation")
        user = User(
            username=validated_data["username"],
            email=validated_data["email"],
            is_student=validated_data.get("is_student", False),
            is_instructor=validated_data.get("is_instructor", False),
        )
        user.set_password(validated_data["password"])
        user.save()
        return user
