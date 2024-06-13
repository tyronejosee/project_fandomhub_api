"""Tests for Models in Genres App."""

from django.test import TestCase
from django.core.exceptions import ValidationError

from ..models import Producer
from ..choices import TypeChoices


class ProducerModelTestCase(TestCase):
    """Test cases for Studio model."""

    def test_creation_producer(self):
        """Test creating a producer."""

        producer = Producer.objects.create(
            name="Studio Ghibli",
            name_jpn="スタジオジブリ",
            established="Jun, 1985",
            type=TypeChoices.STUDIO,
            image=None,
            favorites=123,
        )
        self.assertEqual(producer.name, "Studio Ghibli")
        self.assertEqual(producer.name_jpn, "スタジオジブリ")
        self.assertEqual(producer.established, "Jun, 1985")
        self.assertEqual(producer.type, TypeChoices.STUDIO)
        self.assertEqual(producer.image, None)
        self.assertEqual(producer.favorites, 123)
        self.assertEqual(producer.is_available, True)

    def test_update_studio(self):
        """Test updating a studio."""
        producer = Producer(
            name="MAPPA",
            name_jpn="MAPPA",
            type=TypeChoices.STUDIO,
        )
        producer.save()

        producer.name = "A-1 Pictures"
        producer.full_clean()
        producer.save()
        updated_producer = Producer.objects.get(pk=producer.pk)
        self.assertEqual(updated_producer.name, "A-1 Pictures")

    def test_delete_producer(self):
        """Test deleting a producer."""
        producer = Producer.objects.create(
            name="Bones",
            name_jpn="ボンズ",
            type=TypeChoices.STUDIO,
        )
        producer.save()
        producer.delete()
        with self.assertRaises(Producer.DoesNotExist):
            Producer.objects.get(pk=producer.pk)

    def test_validate_name_field(self):
        """Test name field validation."""
        with self.assertRaises(ValidationError):
            producer1 = Producer(name="Studio Ghibli", name_jpn="スタジオジブリ")
            producer1.save()

            producer2 = Producer(name="Studio Ghibli", name_jpn="Another Name")
            producer2.full_clean()  # Error
