"""Serializers for Contents App."""

from rest_framework import serializers
from apps.categories.models import Url, Studio, Genre, Season, Demographic, Author


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
    image = serializers.CharField(source='get_image')

    class Meta:
        """Meta definition for StudioSerializer."""
        model = Studio
        fields = ('id', 'slug', 'name', 'name_jpn', 'established', 'image',)
        read_only_fields = ('slug',)


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


class DemographicSerializer(serializers.ModelSerializer):
    """Serializer for Demographic model."""

    class Meta:
        """Meta definition for DemographicSerializer."""
        model = Demographic
        fields = ('id', 'name',)


class AuthorSerializer(serializers.ModelSerializer):
    """Serializer for Author model."""

    class Meta:
        """Meta definition for AuthorSerializer."""
        model = Author
        fields = ('id', 'name',)
