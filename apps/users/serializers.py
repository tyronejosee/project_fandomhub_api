"""Serializers for Users App."""

from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer

User = get_user_model()


class UserSerializer(UserCreateSerializer):
    """Serializer for User model."""

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = [
            "id",
            "email",
            "username",
            "created_at",
            "updated_at",
        ]


class UserMinimumSerializer(UserCreateSerializer):
    """Serializer for User model (Minimum)."""

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = [
            "id",
            "username",
        ]
