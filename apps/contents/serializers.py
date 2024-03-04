"""Serializers for Contents App."""

from rest_framework import serializers
from apps.contents.models import Anime, Manga
from apps.categories.serializers import (
    GenreSerializer, StudioListSerializer, SeasonListSerializer,
    DemographicSerializer
)


class AnimeSerializer(serializers.ModelSerializer):
    """Serializer for Anime model."""
    studio = StudioListSerializer()
    genres = GenreSerializer(many=True)
    season = SeasonListSerializer()
    status = serializers.CharField(source="get_status_display")
    category = serializers.CharField(source="get_category_display")

    class Meta:
        """Meta definition for AnimeSerializer."""
        model = Anime
        fields = [
            "id", "name", "name_jpn", "slug", "image", "synopsis", "episodes",
            "duration", "release", "category", "website", "trailer", "status",
            "rating", "studio", "genres", "season",
        ]


class AnimeListSerializer(serializers.ModelSerializer):
    """Serializer for Anime model (List only)."""
    year = serializers.SerializerMethodField()

    class Meta:
        """Meta definition for AnimeListSerializer."""
        model = Anime
        fields = [
            "id", "name", "year", "episodes", "rank",
            "popularity", "num_list_users"
        ]

    def get_year(self, obj):
        return obj.season.year if obj.season else None


class MangaSerializer(serializers.ModelSerializer):
    """Serializer for Manga model."""
    author = serializers.CharField(source="author.name")
    demographic = DemographicSerializer()
    genres = GenreSerializer(many=True)

    class Meta:
        """Meta definition for MangaSerializer."""
        model = Manga
        fields = [
            "id", "name", "name_jpn", "slug", "image", "synopsis",
            "chapters", "release", "media_type", "website", "status",
            "author", "demographic", "genres",
        ]
