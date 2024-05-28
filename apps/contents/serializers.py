"""Serializers for Contents App."""

from rest_framework import serializers

from apps.categories.serializers import (
    GenreReadSerializer,
    StudioReadSerializer,
    SeasonReadSerializer,
    DemographicReadSerializer,
)
from .models import Anime, Manga


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
            "image",
            "synopsis",
            "episodes",
            "duration",
            "release",
            "category",
            "website",
            "trailer",
            "status",
            "rating",
            "studio",
            "genres",
            "season",
            "mean",
            "rank",
            "popularity",
            "favorites",
            "num_list_users",
        ]


class AnimeWriteSerializer(serializers.ModelSerializer):
    """Serializer for Anime model."""

    class Meta:
        model = Anime
        fields = [
            "name",
            "name_jpn",
            "name_rom",
            "image",
            "synopsis",
            "episodes",
            "duration",
            "release",
            "category",
            "website",
            "trailer",
            "status",
            "rating",
            "studio",
            "genres",
            "season",
        ]


class AnimeMinimalSerializer(serializers.ModelSerializer):
    """Serializer for Anime model (Minimal)."""

    class Meta:
        model = Anime
        fields = [
            "id",
            "name",
            "image",
            "episodes",
            "rank",
            "popularity",
            "num_list_users",
        ]

    # def get_year(self, obj):
    #     return int(obj.season.year if obj.season else None)


class MangaReadSerializer(serializers.ModelSerializer):
    """Serializer for Manga model (Retrieve)."""

    author = serializers.CharField(source="author.name")
    demographic = DemographicReadSerializer()
    genres = GenreReadSerializer(many=True)

    class Meta:
        model = Manga
        fields = [
            "id",
            "name",
            "name_jpn",
            "slug",
            "image",
            "synopsis",
            "chapters",
            "release",
            "media_type",
            "website",
            "status",
            "author",
            "demographic",
            "genres",
        ]


class MangaWriteSerializer(serializers.ModelSerializer):
    """Serializer for Manga model (Create/update)."""

    class Meta:
        model = Manga
        fields = [
            "name",
            "name_jpn",
            "name_rom",
            "slug",
            "image",
            "synopsis",
            "chapters",
            "release",
            "media_type",
            "website",
            "status",
            "author",
            "demographic",
            "genres",
            "themes",
        ]


class MangaMinimalSerializer(serializers.ModelSerializer):
    """Serializer for Anime model (Minimal)."""

    class Meta:
        model = Manga
        fields = [
            "id",
            "name",
            "image",
            "release",
            "media_type",
            "status",
        ]
