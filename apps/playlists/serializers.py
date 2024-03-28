"""Serializers for Playlists App."""

from django.shortcuts import get_object_or_404
from rest_framework import serializers

from apps.contents.models import Anime, Manga
from apps.contents.serializers import (
    AnimeMinimumSerializer, MangaMinimumSerializer
)
from .models import Playlist, PlaylistAnime, PlaylistManga


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
    anime_id = serializers.UUIDField(write_only=True)
    anime = AnimeMinimumSerializer(read_only=True)

    class Meta:
        """Meta definition for PlaylistAnimeSerializer."""
        model = PlaylistAnime
        fields = [
            "id", "anime", "anime_id", "status", "is_watched", "is_favorite"
        ]  # Add order field

        def create(self, validated_data):
            anime_id = validated_data.pop("anime_id")
            anime = get_object_or_404(Anime, id=anime_id)
            playlist_anime = PlaylistAnime.objects.create(
                anime=anime,
                **validated_data,
            )
            return playlist_anime


class PlaylistMangaSerializer(serializers.ModelSerializer):
    """Serializer for PlaylistManga model."""
    manga_id = serializers.UUIDField(write_only=True)
    manga = MangaMinimumSerializer(read_only=True)

    class Meta:
        """Meta definition for PlaylistMangaSerializer."""
        model = PlaylistManga
        fields = [
            "id", "manga", "manga_id", "status", "is_watched", "is_favorite"
        ]  # Add order field

        def create(self, validated_data):
            manga_id = validated_data.pop("manga_id")
            manga = get_object_or_404(Manga, id=manga_id)
            playlist_manga = PlaylistManga.objects.create(
                manga=manga,
                **validated_data,
            )
            return playlist_manga
