"""Serializer Tests for Characters App."""

import pytest

from ..serializers import (
    CharacterReadSerializer,
    CharacterWriteSerializer,
    CharacterMinimalSerializer,
    CharacterVoiceReadSerializer,
)


@pytest.mark.django_db
class TestCharacterSerializers:
    """Tests for Character serializers."""

    def test_character_read_serializer(self, character):
        serializer = CharacterReadSerializer(character)
        expected_data = {
            "id": str(character.id),
            "name": character.name,
            "name_kanji": character.name_kanji,
            "favorites": character.favorites,
            "about": character.about,
            "role": character.role,
            "image": character.image.url,
            "created_at": character.created_at.isoformat(),
            "updated_at": character.updated_at.isoformat(),
        }

        assert serializer.data == expected_data

    def test_character_write_serializer_valid_data(self, character):
        data = {
            "name": "Naruto Uzumaki",
            "name_kanji": character.name_kanji,
            "about": character.about,
            "role": character.role,
            "image": character.image,
        }
        serializer = CharacterWriteSerializer(data=data)

        assert serializer.is_valid(), serializer.errors
        assert serializer.validated_data["name"] == "Naruto Uzumaki"
        assert serializer.validated_data["image"]

    def test_character_write_serializer_invalid_data(self):
        data = {}
        serializer = CharacterWriteSerializer(data=data)

        assert not serializer.is_valid()
        assert "name" in serializer.errors
        assert "name_kanji" in serializer.errors
        assert "role" in serializer.errors
        assert "image" in serializer.errors

    def test_character_minimal_serializer(self, character):
        serializer = CharacterMinimalSerializer(character)
        expected_data = {
            "id": str(character.id),
            "name": character.name,
            "role": character.get_role_display(),
            "image": character.image.url,
            "created_at": character.created_at.isoformat(),
            "favorites": character.favorites,
        }

        assert serializer.data == expected_data


@pytest.mark.django_db
class TestCharacterVoiceSerializers:
    """Tests for CharacterVoice serializers."""

    def test_character_voice_read_serializer(self, character_voice):
        serializer = CharacterVoiceReadSerializer(character_voice)
        expected_data = {
            "id": str(character_voice.id),
            "character_id": {
                "id": str(character_voice.character_id.id),
                "name": character_voice.character_id.name,
                "role": character_voice.character_id.get_role_display(),
                "image": character_voice.character_id.image.url,
                "created_at": character_voice.character_id.created_at.isoformat(),
                "favorites": character_voice.character_id.favorites,
            },
        }

        assert serializer.data == expected_data
