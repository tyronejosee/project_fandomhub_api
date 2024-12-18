"""Serializers for Users App."""

from django.contrib.auth import get_user_model
from rest_framework import serializers
from djoser.serializers import UserCreateSerializer

from apps.utils.mixins import ReadOnlyFieldsMixin

User = get_user_model()


class UserReadSerializer(UserCreateSerializer):
    """Serializer for User model."""

    role = serializers.CharField(source="get_role_display")

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = [
            "id",
            "email",
            "username",
            "role",
            "is_online",
            "is_active",
            "is_staff",
            "created_at",
            "updated_at",
        ]


class UserWriteSerializer(UserCreateSerializer):
    """Serializer for User model."""

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = [
            "email",
            "username",
            "role",
            "is_online",
            "is_active",
            "is_staff",
        ]


class UserMinimalSerializer(ReadOnlyFieldsMixin, UserCreateSerializer):
    """Serializer for User model (Minimal)."""

    role = serializers.CharField(source="get_role_display")

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = [
            "id",
            "username",
            "role",
            "is_online",
        ]
