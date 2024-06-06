"""Tests for Models in Genres App."""

from django.test import TestCase
from django.core.exceptions import ValidationError

from ..models import Studio


class StudioModelTestCase(TestCase):
    """Test cases for Studio model."""

    def test_creation_studio(self):
        """Test creating a studio."""

        studio = Studio.objects.create(
            name="Studio Ghibli",
            name_jpn="スタジオジブリ",
            established="Jun, 1985",
            image=None,
        )
        self.assertEqual(studio.name, "Studio Ghibli")
        self.assertEqual(studio.name_jpn, "スタジオジブリ")
        self.assertEqual(studio.established, "Jun, 1985")
        self.assertEqual(studio.is_available, True)
        self.assertEqual(studio.image, None)

    def test_update_studio(self):
        """Test updating a studio."""
        studio = Studio(name="MAPPA", name_jpn="MAPPA")
        studio.save()

        studio.name = "A-1 Pictures"
        studio.full_clean()
        studio.save()
        updated_studio = Studio.objects.get(pk=studio.pk)
        self.assertEqual(updated_studio.name, "A-1 Pictures")

    def test_delete_studio(self):
        """Test deleting a studio."""
        studio = Studio(name="Bones", name_jpn="ボンズ")
        studio.save()
        studio.delete()
        with self.assertRaises(Studio.DoesNotExist):
            Studio.objects.get(pk=studio.pk)

    def test_validate_name_field(self):
        """Test name field validation."""
        with self.assertRaises(ValidationError):
            studio1 = Studio(name="Studio Ghibli", name_jpn="スタジオジブリ")
            studio1.save()

            studio2 = Studio(name="Studio Ghibli", name_jpn="Another Name")
            studio2.full_clean()  # Error
