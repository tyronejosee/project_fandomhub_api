"""Serializers for Mangas App."""

from rest_framework import serializers

from apps.categories.serializers import DemographicReadSerializer
from apps.genres.serializers import GenreReadSerializer
from .models import Manga


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
        extra_kwargs = {
            "image": {"required": True},
        }


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
