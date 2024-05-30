"""Serializers for Animes App."""

from rest_framework import serializers

from apps.categories.serializers import (
    GenreReadSerializer,
    StudioReadSerializer,
    SeasonReadSerializer,
)
from .models import Anime


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
            "rank",
            "popularity",
            "num_list_users",
        ]

    # def get_year(self, obj):
    #     return int(obj.season.year if obj.season else None)
