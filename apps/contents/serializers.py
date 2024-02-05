"""Serializers for Contents App."""

from rest_framework import serializers
from apps.contents.models import (
    Url, Studio, Genre, Season, Rating, Anime,
)


class UrlSerializer(serializers.ModelSerializer):
    """Serializer for Url model."""

    class Meta:
        """Meta definition for UrlSerializer."""
        model = Url
        fields = ('tag', 'url')

    def to_representation(self,instance):
        return {
            'id': instance.id,
            'tag': instance.get_tag_display(),
            'url': instance.url,
        }


class StudioSerializer(serializers.ModelSerializer):
    """Serializer for Studio model."""

    class Meta:
        """Meta definition for StudioSerializer."""
        model = Studio
        fields = (
            'id', 'slug', 'name', 'name_jpn', 'established', 'image',
        )
        read_only_fields = ('slug',)

    # add to representation for image field


class GenreSerializer(serializers.ModelSerializer):
    """Serializer for Genre model."""

    class Meta:
        """Meta definition for GenreSerializer."""
        model = Genre
        fields = ('id', 'name', 'slug',)
        read_only_fields = ('slug',)


class SeasonSerializer(serializers.ModelSerializer):
    """Serializer for Season model."""

    class Meta:
        """Meta definition for SeasonSerializer."""
        model = Season
        fields = ('id', 'name', 'slug',)
        read_only_fields = ('slug',)


class RatingSerializer(serializers.ModelSerializer):
    """Serializer for Rating model."""

    class Meta:
        """Meta definition for RatingSerializer."""
        model = Rating
        fields = ('id', 'name',)


class AnimeSerializer(serializers.ModelSerializer):
    """Serializer for Anime model."""
    status = serializers.CharField(source='get_status_display')
    category = serializers.CharField(source='get_category_display')
    # studio_id = StudioSerializer()
    # genre_id = GenreSerializer()
    # season_id = SeasonSerializer()
    # rating_id = RatingSerializer()
    # url_id = UrlSerializer(many=True)

    class Meta:
        """Meta definition for AnimeSerializer."""
        model = Anime
        fields = [
            'id', 'name', 'name_jpn', 'slug', 'image', 'synopsis', 'episodes',
            'duration', 'release', 'category', 'status', 'studio_id',
            'genre_id', 'season_id', 'rating_id', 'url_id',
        ]

    # Add to representation
