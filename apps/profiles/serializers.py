"""Serializers for Profiles App."""

from rest_framework import serializers

from apps.users.serializers import UserMinimumSerializer
from .models import Profile


class ProfileReadSerializer(serializers.ModelSerializer):
    """Serializer for Profile model (List/retrieve)."""

    user_id = UserMinimumSerializer()

    class Meta:
        model = Profile
        fields = [
            "id",
            "user_id",
            "first_name",
            "last_name",
            "birth_date",
            "bio",
            "image",
            "cover",
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["image"] = representation.get("image", "") or ""
        representation["cover"] = representation.get("image", "") or ""
        return representation


class ProfileWriteSerializer(serializers.ModelSerializer):
    """Serializer for Profile model (Update)."""

    class Meta:
        model = Profile
        fields = [
            "first_name",
            "last_name",
            "birth_date",
            "bio",
            "image",
            "cover",
        ]
        extra_kwargs = {
            "image": {"required": True},
        }


class ProfileMinimalSerializer(serializers.ModelSerializer):
    """Serializer for Profile model (Minimal)."""

    user_id = UserMinimumSerializer()

    class Meta:
        model = Profile
        fields = [
            "id",
            "user_id",
            "first_name",
            "last_name",
            "image",
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["image"] = representation.get("image", "") or ""
        return representation
