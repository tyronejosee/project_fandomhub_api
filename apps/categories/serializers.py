"""Serializers for Categories App."""

from rest_framework import serializers

from apps.utils.validators import validate_name
from .models import Theme, Demographic


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


class DemographicReadSerializer(serializers.ModelSerializer):
    """Serializer for Demographic model (List/Retrieve)."""

    name = serializers.CharField(validators=[validate_name])

    class Meta:
        model = Demographic
        fields = [
            "id",
            "name",
            "slug",
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
