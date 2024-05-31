"""Tests for Models in Genres App."""

from django.test import TestCase

from ..models import Genre


class GenreModelTestCase(TestCase):
    """Test cases for Genre model."""

    def test_creation_genre(self):
        """Test creating a studio."""
        genre = Genre.objects.create(name="Romance")
        self.assertEqual(genre.name, "Romance")
        self.assertEqual(genre.available, True)

    def test_update_genre(self):
        """Test updating a genre."""
        genre = Genre(name="Drama")
        genre.save()

        genre.name = "Adventure"
        genre.full_clean()
        genre.save()

        updated_genre = Genre.objects.get(pk=genre.pk)
        self.assertEqual(updated_genre.name, "Adventure")
        self.assertNotEqual(updated_genre.name, "Drama")

    def test_delete_genre(self):
        """Test deleting a genre."""
        genre = Genre(name="Action")
        genre.save()
        genre.delete()

        with self.assertRaises(Genre.DoesNotExist):
            Genre.objects.get(pk=genre.pk)
