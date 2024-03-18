"""Serializers for Reviesws App."""

from rest_framework.serializers import ModelSerializer
from apps.users.serializers import UserSerializer
from apps.contents.serializers import AnimeListSerializer
from .models import Review


class ReviewSerializer(ModelSerializer):
    """Serializer for Review model."""
    user = UserSerializer()
    anime = AnimeListSerializer()

    class Meta:
        """Meta definition for ReviewSerializer."""
        model = Review
        fields = [
            "id", "user", "anime", "rating", "comment",
            "available", "created_at", "updated_at"
        ]
