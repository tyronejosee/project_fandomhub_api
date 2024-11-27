"""Serializer Tests for Producers App."""

import pytest

from ..serializers import ProducerReadSerializer, ProducerWriteSerializer


@pytest.mark.django_db
class TestProducerSerializers:
    """Tests for Producer serializers."""

    def test_producer_read_serializer(self, producer):
        serializer = ProducerReadSerializer(producer)
        expected_data = {
            "id": str(producer.id),
            "name": producer.name,
            "name_jpn": producer.name_jpn,
            "slug": producer.slug,
            "about": producer.about,
            "established": producer.established,
            "type": producer.type,
            "image": producer.image.url,
            "favorites": producer.favorites,
            "created_at": producer.created_at.isoformat(),
            "updated_at": producer.updated_at.isoformat(),
        }

        assert serializer.data == expected_data

    def test_producer_write_serializer_valid_data(self, producer):
        data = {
            "name": "Wit Studio",
            "name_jpn": "ウィットスタジオ",
            "about": producer.about,
            "established": producer.established,
            "type": producer.type,
            "image": producer.image,
        }
        serializer = ProducerWriteSerializer(data=data)

        assert serializer.is_valid()
        assert serializer.validated_data["name"] == "Wit Studio"
        assert serializer.validated_data["name_jpn"] == "ウィットスタジオ"

    def test_producer_write_serializer_invalid_data(self):
        data = {}
        serializer = ProducerWriteSerializer(data=data)

        assert not serializer.is_valid()
        assert "name" in serializer.errors
        assert "name_jpn" in serializer.errors
        assert "type" in serializer.errors
        assert "image" in serializer.errors
