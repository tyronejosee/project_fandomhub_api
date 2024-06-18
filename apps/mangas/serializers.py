"""Serializers for Mangas App."""

from rest_framework import serializers

from apps.genres.serializers import GenreReadSerializer, DemographicReadSerializer
from .models import Magazine, Manga, MangaStats


class MagazineReadSerializer(serializers.ModelSerializer):
    """Serializer for Magazine model (List/retrieve)."""

    class Meta:
        model = Magazine
        fields = [
            "id",
            "name",
            "slug",
            "count",
            "created_at",
            "updated_at",
        ]


class MagazineWriteSerializer(serializers.ModelSerializer):
    """Serializer for Magazine model (Create/update)."""

    class Meta:
        model = Magazine
        fields = [
            "name",
        ]


class MangaReadSerializer(serializers.ModelSerializer):
    """Serializer for Manga model (Retrieve)."""

    author_id = serializers.CharField(source="author.name")
    demographic_id = DemographicReadSerializer()
    genres = GenreReadSerializer(many=True)
    media_type = serializers.CharField(source="get_media_type_display")
    status = serializers.CharField(source="get_status_display")

    class Meta:
        model = Manga
        fields = [
            "id",
            "name",
            "name_jpn",
            "name_rom",
            "alternative_names",
            "slug",
            "image",
            "synopsis",
            "background",
            "media_type",
            "volumes",
            "chapters",
            "status",
            "published_from",
            "published_to",
            "genres",
            "themes",
            "demographic_id",
            "serialization_id",
            "author_id",
            "website",
            "is_recommended",
            "score",
            "ranked",
            "popularity",
            "members",
            "favorites",
            "created_at",
            "updated_at",
        ]


class MangaWriteSerializer(serializers.ModelSerializer):
    """Serializer for Manga model (Create/update)."""

    class Meta:
        model = Manga
        fields = [
            "name",
            "name_jpn",
            "name_rom",
            "alternative_names",
            "image",
            "synopsis",
            "background",
            "media_type",
            "volumes",
            "chapters",
            "status",
            "published_from",
            "published_to",
            "genres",
            "themes",
            "demographic_id",
            "serialization_id",
            "author_id",
            "website",
        ]
        extra_kwargs = {
            "image": {"required": True},
        }


class MangaMinimalSerializer(serializers.ModelSerializer):
    """Serializer for Anime model (Minimal)."""

    media_type = serializers.CharField(source="get_media_type_display")
    status = serializers.CharField(source="get_status_display")

    class Meta:
        model = Manga
        fields = [
            "id",
            "name",
            "image",
            "published_from",
            "published_to",
            "media_type",
            "status",
        ]


class MangaStatsReadSerializer(serializers.ModelSerializer):
    """Serializer for MangaStats model (List/retrieve)."""

    class Meta:
        model = MangaStats
        fields = [
            "id",
            "reading",
            "completed",
            "on_hold",
            "dropped",
            "plan_to_read",
            "total",
            "updated_at",
        ]
