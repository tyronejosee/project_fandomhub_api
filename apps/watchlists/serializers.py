"""Serializers for Watchlists App."""

from rest_framework import serializers
from apps.watchlists.models import AnimeWatchlist, MangaWatchlist


class AnimeWatchlistSerializer(serializers.ModelSerializer):
    """Serializer for AnimeWatchlist model."""
    status = serializers.CharField(source="get_status_display")

    class Meta:
        """Meta definition for AnimeWatchlistSerializer."""
        model = AnimeWatchlist
        fields = [
            "id", "user", "status", "anime", "is_watched", "score",
            "priority", "tags", "comments"
        ]


class MangaWatchlistSerializer(serializers.ModelSerializer):
    """Serializer for MangaWatchlist model."""
    status = serializers.CharField(source="get_status_display")

    class Meta:
        """Meta definition for MangaWatchlistSerializer."""
        model = MangaWatchlist
        fields = [
            "id", "user", "manga", "status", "is_watched", "score",
            "priority", "tags", "comments"
        ]
