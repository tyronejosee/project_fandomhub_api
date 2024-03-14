"""Serializers for Playlists App."""

from rest_framework import serializers
from apps.playlists.models import Playlist, PlaylistAnime
from apps.contents.serializers import (
    AnimeMinimumSerializer, MangaMinimumSerializer
)


class PlaylistSerializer(serializers.ModelSerializer):
    """Serializer for Playlist model."""

    class Meta:
        """Meta definition for PlaylistSerializer."""
        model = Playlist
        fields = [
            "id", "name", "created_at"
        ]


class PlaylistAnimeSerializer(serializers.ModelSerializer):
    """Serializer for PlaylistAnime model."""
    anime = AnimeMinimumSerializer()

    class Meta:
        """Meta definition for PlaylistAnimeSerializer."""
        model = PlaylistAnime
        fields = [
            "id", "playlist", "anime", "status", "is_watched", "is_favorite"
        ]    # Add order field


class PlaylistMangaSerializer(serializers.ModelSerializer):
    """Serializer for PlaylistManga model."""
    manga = MangaMinimumSerializer()

    class Meta:
        """Meta definition for PlaylistMangaSerializer."""
        model = PlaylistAnime
        fields = [
            "id", "playlist", "manga", "status", "is_watched", "is_favorite"
        ]   # Add order field
