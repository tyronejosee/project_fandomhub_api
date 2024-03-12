"""Serializers for Playlists App."""

from rest_framework import serializers
from apps.playlists.models import Playlist, PlaylistAnime
from apps.contents.serializers import AnimeListSerializer


# class MangaWatchlistSerializer(serializers.ModelSerializer):
#     """Serializer for MangaWatchlist model."""
#     status = serializers.CharField(source="get_status_display")

#     class Meta:
#         """Meta definition for MangaWatchlistSerializer."""
#         model = MangaWatchlist
#         fields = [
#             "id", "user", "manga", "status", "is_watched", "score",
#             "priority", "tags", "comments"
#         ]


class PlaylistAnimeSerializer(serializers.ModelSerializer):
    """Pending."""
    anime = AnimeListSerializer()

    class Meta:
        """Pending."""
        model = PlaylistAnime
        fields = ["id", "rating", "status", "score", "anime"]


class PlaylistSerializer(serializers.ModelSerializer):
    """Pending."""

    class Meta:
        """Pending."""
        model = Playlist
        fields = "__all__"
