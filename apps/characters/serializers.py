"""Serializers for Characters App."""

from rest_framework import serializers

from .models import Character


class CharacterReadSerializer(serializers.ModelSerializer):
    """Serializer for Character model (List/Retrieve)."""

    class Meta:
        model = Character
        fields = [
            "id",
            "name",
            "name_kanji",
            "favorites",
            "about",
            "role",
            "image",
            "created_at",
            "updated_at",
        ]


class CharacterWriteSerializer(serializers.ModelSerializer):
    """Serializer for Character model (Create/update)."""

    class Meta:
        model = Character
        fields = [
            "name",
            "name_kanji",
            "about",
            "role",
            "image",
        ]
        extra_kwargs = {
            "image": {"required": True},
        }
