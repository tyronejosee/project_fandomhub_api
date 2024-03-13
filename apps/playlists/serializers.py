"""Serializers for Playlists App."""

from rest_framework import serializers
from apps.playlists.models import Playlist, PlaylistItem
from apps.contents.serializers import (
    AnimeMinimumSerializer, MangaMinimumSerializer
)


class PlaylistSerializer(serializers.ModelSerializer):
    """Serializer for Playlist model."""

    class Meta:
        """Pending."""
        model = Playlist
        fields = [
            "id", "name", "user", "created_at", "anime_items", "manga_items"
        ]


class PlaylistItemSerializer(serializers.ModelSerializer):
    """Serializer for PlaylistItem model."""
    anime = AnimeMinimumSerializer()
    manga = MangaMinimumSerializer()

    class Meta:
        """Pending."""
        model = PlaylistItem
        fields = [
            "id", "playlist", "anime", "manga", "status", "is_watched"
        ]
