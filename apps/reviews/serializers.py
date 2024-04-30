"""Serializers for Reviews App."""

from rest_framework.serializers import ModelSerializer

from apps.users.serializers import UserListSerializer
from .models import ReviewAnime, ReviewManga


class ReviewAnimeSerializer(ModelSerializer):
    """Serializer for ReviewAnime model."""
    user = UserListSerializer(read_only=True)
    # TODO: Add image field to the user

    class Meta:
        """Meta definition for ReviewAnimeSerializer."""
        model = ReviewAnime
        fields = [
            "id",
            "user",
            "comment",
            "rating",
            "created_at",
            "updated_at"
        ]


class ReviewMangaSerializer(ModelSerializer):
    """Serializer for ReviewManga model."""
    user = UserListSerializer(read_only=True)
    # TODO: Add image field to the user

    class Meta:
        """Meta definition for ReviewMangaSerializer."""
        model = ReviewManga
        fields = [
            "id",
            "user",
            "comment",
            "rating",
            "created_at",
            "updated_at"
        ]
