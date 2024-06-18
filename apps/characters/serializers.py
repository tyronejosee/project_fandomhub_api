"""Serializers for Characters App."""

from rest_framework import serializers

from .models import Character, CharacterVoice


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


class CharacterMinimalSerializer(serializers.ModelSerializer):
    """Serializer for Character model (Minimal)."""

    role = serializers.CharField(source="get_role_display")

    class Meta:
        model = Character
        fields = [
            "id",
            "name",
            "role",
            "image",
            "created_at",
        ]


class CharacterVoiceReadSerializer(serializers.ModelSerializer):
    """Serializer for CharacterVoice model (List)."""

    character_id = CharacterMinimalSerializer()

    class Meta:
        model = CharacterVoice
        fields = [
            "id",
            "character_id",
        ]
