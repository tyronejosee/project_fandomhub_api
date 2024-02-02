"""Serializers for Contents App."""

from rest_framework import serializers
from apps.contents.models import (
    Url, Studio, Genre, Premiered, Rating, Content,
)


class UrlSerializer(serializers.ModelSerializer):
    """Serializer for Url model."""

    class Meta:
        """Meta definition for UrlSerializer."""
        model = Url
        fields = '__all__'


class StudioSerializer(serializers.ModelSerializer):
    """Serializer for Studio model."""

    class Meta:
        """Meta definition for StudioSerializer."""
        model = Studio
        fields = (
            'id', 'slug', 'name', 'name_jpn', 'established', 'image',
            'created_at', 'updated_at'
        )
        read_only_fields = ('slug', 'created_at', 'updated_at')


class GenreSerializer(serializers.ModelSerializer):
    """Serializer for Genre model."""

    class Meta:
        """Meta definition for GenreSerializer."""
        model = Genre
        fields = '__all__'


class PremieredSerializer(serializers.ModelSerializer):
    """Serializer for Premiered model."""

    class Meta:
        """Meta definition for PremieredSerializer."""
        model = Premiered
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    """Serializer for Rating model."""

    class Meta:
        """Meta definition for RatingSerializer."""
        model = Rating
        fields = '__all__'


class ContentSerializer(serializers.ModelSerializer):
    """Serializer for Content model."""

    class Meta:
        """Meta definition for ContentSerializer."""
        model = Content
        fields = '__all__'
