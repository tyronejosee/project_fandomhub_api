"""Serializers for Animes App."""

from rest_framework import serializers

from apps.studios.serializers import StudioReadSerializer
from apps.genres.serializers import GenreReadSerializer
from apps.seasons.serializers import SeasonReadSerializer
from .models import Anime, AnimeStats


class AnimeReadSerializer(serializers.ModelSerializer):
    """Serializer for Anime model."""

    studio = StudioReadSerializer()
    genres = GenreReadSerializer(many=True)
    season = SeasonReadSerializer()
    status = serializers.CharField(source="get_status_display")
    category = serializers.CharField(source="get_category_display")

    class Meta:
        model = Anime
        fields = [
            "id",
            "name",
            "name_jpn",
            "name_rom",
            "slug",
            "alternative_names",
            "image",
            "trailer",
            "synopsis",
            "media_type",
            "episodes",
            "status",
            "release",
            "season",
            "studio",
            "source",
            "genres",
            "themes",
            "duration",
            "rating",
            "website",
            "is_recommended",
            "score",
            "ranked",
            "popularity",
            "members",
            "favorites",
        ]


class AnimeWriteSerializer(serializers.ModelSerializer):
    """Serializer for Anime model."""

    class Meta:
        model = Anime
        fields = [
            "name",
            "name_jpn",
            "name_rom",
            "alternative_names",
            "image",
            "trailer",
            "synopsis",
            "media_type",
            "episodes",
            "status",
            "release",
            "season",
            "studio",
            "source",
            "genres",
            "themes",
            "duration",
            "rating",
            "website",
        ]
        extra_kwargs = {
            "image": {"required": True},
        }


class AnimeMinimalSerializer(serializers.ModelSerializer):
    """Serializer for Anime model (Minimal)."""

    class Meta:
        model = Anime
        fields = [
            "id",
            "name",
            "image",
            "episodes",
            "ranked",
            "popularity",
            "members",
        ]


class AnimeStatsReadSerializer(serializers.ModelSerializer):
    """Serializer for AnimeStats model (List/retrieve)."""

    class Meta:
        model = AnimeStats
        fields = [
            "id",
            "watching",
            "completed",
            "on_hold",
            "dropped",
            "plan_to_watch",
            "total",
            "updated_at",
        ]
