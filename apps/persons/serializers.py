"""Serializers for Persons App."""

from rest_framework import serializers

from .models import Person


class PersonSerializer(serializers.ModelSerializer):
    """Serializer for Person model."""

    class Meta:
        model = Person
        fields = [
            "id",
            "name",
        ]


class PersonReadSerializer(serializers.ModelSerializer):
    """Serializer for Person model (List/retrieve)."""

    class Meta:
        model = Person
        fields = [
            "id",
            "name",
            "slug",
            "given_name",
            "family_name",
            "image",
            "alternate_names",
            "birthday",
            "about",
            "website",
            "language",
            "category",
            "favorites",
            "created_at",
            "updated_at",
        ]
        extra_kwargs = {
            "image": {"required": True},
        }


class PersonMinimalSerializer(serializers.ModelSerializer):
    """Serializer for Person model (Minimal)."""

    language = serializers.CharField(source="get_language_display")

    class Meta:
        model = Person
        fields = [
            "id",
            "name",
            "image",
            "language",
        ]
