"""Serializers for Contents App."""

from rest_framework import serializers
from apps.contents.models import Anime, Manga


class AnimeSerializer(serializers.ModelSerializer):
    """Serializer for Anime model."""
    image = serializers.CharField(source='get_image')
    status = serializers.CharField(source='get_status_display')
    category = serializers.CharField(source='get_category_display')

    class Meta:
        """Meta definition for AnimeSerializer."""
        model = Anime
        fields = [
            'id', 'name', 'name_jpn', 'slug', 'image', 'synopsis', 'episodes',
            'duration', 'release', 'category', 'status', 'rating', 'studio_id',
            'genre_id', 'season_id', 'url_id',
        ]


class MangaSerializer(serializers.ModelSerializer):
    """Serializer for Manga model."""
    image = serializers.CharField(source='get_image')

    class Meta:
        """Meta definition for MangaSerializer."""
        model = Manga
        fields = [
            'id', 'name', 'name_jpn', 'slug', 'image', 'synopsis', 'chapters',
            'release', 'category', 'status', 'author_id', 'demographic_id',
            'genre_id', 'url_id',
        ]
