"""Serializers for Animes App."""

from rest_framework import serializers

from apps.producers.serializers import ProducerReadSerializer
from apps.genres.serializers import GenreReadSerializer, GenreMinimalSerializer
from .models import Anime, AnimeStats


class AnimeReadSerializer(serializers.ModelSerializer):
    """Serializer for Anime model."""

    studio_id = ProducerReadSerializer()
    genres = GenreReadSerializer(many=True)
    status = serializers.CharField(source="get_status_display")

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
            "background",
            "season",
            "year",
            "broadcast_id",
            "media_type",
            "episodes",
            "status",
            "aired_from",
            "aired_to",
            "studio_id",
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
            "background",
            "season",
            "year",
            "broadcast_id",
            "media_type",
            "episodes",
            "status",
            "aired_from",
            "aired_to",
            "studio_id",
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

    genres = GenreMinimalSerializer(many=True)

    class Meta:
        model = Anime
        fields = [
            "id",
            "name",
            "image",
            "episodes",
            "aired_from",
            "year",
            "genres",
            "duration",
            "score",
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
