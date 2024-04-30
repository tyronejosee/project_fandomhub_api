"""Serializers for Users App."""

from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer

User = get_user_model()


class UserSerializer(UserCreateSerializer):
    """Serializer for User model."""

    class Meta(UserCreateSerializer.Meta):
        """Meta definition for UserSerializer."""
        model = User
        fields = [
            "id", "email", "username", "first_name",
            "last_name", "date_joined"
        ]


class UserListSerializer(UserCreateSerializer):
    """Serializer for User model."""

    class Meta(UserCreateSerializer.Meta):
        """Meta definition for UserSerializer."""
        model = User
        fields = [
            "id",
            "username",
        ]  # TODO: Add image field to the user
