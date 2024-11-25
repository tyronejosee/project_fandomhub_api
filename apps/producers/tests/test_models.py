"""Model Tests for Genres App."""

import pytest
from django.db import IntegrityError

from ..models import Producer


@pytest.mark.django_db
class TestProducerModel:
    """Tests for Producer model."""

    def test_producer_creation(self, producer):
        producer = Producer.objects.create(
            name="Wit Studio",
            name_jpn="ウィットスタジオ",
            about=producer.about,
            established=producer.established,
            type=producer.type,
            image=producer.image,
        )
        assert producer.name == "Wit Studio"
        assert str(producer) == "Wit Studio"

    def test_producer_unique_fields(self, producer):
        with pytest.raises(IntegrityError):
            Producer.objects.create(
                name=producer.name,
                name_jpn=producer.name_jpn,
                about=producer.about,
                established=producer.established,
                type=producer.type,
                image=producer.image,
            )

    def test_producer_slug_generation(self, producer):
        producer = Producer.objects.create(
            name="Wit Studio",
            name_jpn="ウィットスタジオ",
            about=producer.about,
            established=producer.established,
            type=producer.type,
            image=producer.image,
        )
        assert producer.slug == "wit-studio"

    def test_manager_get_available(self, producer):
        results = Producer.objects.get_available()
        assert results.count() == 1
