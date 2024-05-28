"""Serializers for Contents App."""

from rest_framework import serializers

from apps.utils.validators import validate_name
from .models import Studio, Genre, Theme, Season, Demographic


class StudioReadSerializer(serializers.ModelSerializer):
    """Serializer for Studio model (List/Retrieve)."""

    class Meta:
        model = Studio
        fields = [
            "id",
            "name",
            "name_jpn",
            "slug",
            "established",
            "image",
            "created_at",
            "updated_at",
        ]


class StudioWriteSerializer(serializers.ModelSerializer):
    """Serializer for Studio model (Create/update)."""

    name = serializers.CharField(validators=[validate_name])

    class Meta:
        model = Studio
        fields = [
            "name",
            "name_jpn",
            "established",
            "image",
        ]
        extra_kwargs = {
            "image": {"required": True},
        }


class GenreReadSerializer(serializers.ModelSerializer):
    """Serializer for Genre model (List/retrieve)."""

    class Meta:
        model = Genre
        fields = [
            "id",
            "name",
            "slug",
            "created_at",
            "updated_at",
        ]


class GenreWriteSerializer(serializers.ModelSerializer):
    """Serializer for Genre model (Create/update)."""

    name = serializers.CharField(validators=[validate_name])

    class Meta:
        model = Genre
        fields = [
            "name",
        ]


class ThemeReadSerializer(serializers.ModelSerializer):
    """Serializer for Theme model (List/Retrieve)."""

    class Meta:
        model = Theme
        fields = [
            "id",
            "name",
            "slug",
            "created_at",
            "updated_at",
        ]


class ThemeWriteSerializer(serializers.ModelSerializer):
    """Serializer for Theme model (Create/update)."""

    name = serializers.CharField(validators=[validate_name])

    class Meta:
        model = Theme
        fields = [
            "name",
        ]


class SeasonReadSerializer(serializers.ModelSerializer):
    """Serializer for Season model (List/Retrieve)."""

    class Meta:
        model = Season
        fields = [
            "id",
            "season",
            "year",
            "fullname",
            "created_at",
            "updated_at",
        ]


class SeasonWriteSerializer(serializers.ModelSerializer):
    """Serializer for Season model (Create/update)."""

    class Meta:
        model = Season
        fields = [
            "season",
            "year",
        ]


class DemographicReadSerializer(serializers.ModelSerializer):
    """Serializer for Demographic model (List/Retrieve)."""

    name = serializers.CharField(validators=[validate_name])

    class Meta:
        model = Demographic
        fields = [
            "id",
            "name",
            "created_at",
            "updated_at",
        ]


class DemographicWriteSerializer(serializers.ModelSerializer):
    """Serializer for Demographic model (Create/update)."""

    name = serializers.CharField(validators=[validate_name])

    class Meta:
        model = Demographic
        fields = [
            "name",
        ]
