"""Tests for Models in Categories App."""

from django.test import TestCase
from django.db.utils import IntegrityError
from apps.categories.models import Studio, Genre


class StudioModelTestCase(TestCase):
    """Test cases for Studio model."""

    def setUp(self):
        self.studio = Studio.objects.create(
            name="Studio Name",
            name_jpn="Studio Name JPN",
            established="Studio Established",
            image=None
        )

    def test_creation(self):
        """Test creation of a Studio instance."""
        self.assertEqual(self.studio.name, "Studio Name")
        self.assertEqual(self.studio.name_jpn, "Studio Name JPN")
        self.assertEqual(self.studio.established, "Studio Established")
        self.assertEqual(self.studio.image, None)

    def test_unique_name(self):
        """Test that a Studio with a duplicate name cannot be created."""
        with self.assertRaises(IntegrityError):
            Studio.objects.create(
                name="Studio Name",
                name_jpn="Studio Name JPN",
            )

    def test_str_method(self):
        """Test srt method."""
        studio = Studio.objects.get(name="Studio Name")
        self.assertEqual(str(studio), "Studio Name")

    def test_query(self):
        """Test querying for Studio objects."""
        Studio.objects.create(
            name="Query Example One",
            name_jpn="Query Example One",
        )
        Studio.objects.create(
            name="Query Example Two",
            name_jpn="Query Example Two",
        )
        studios = Studio.objects.filter(name__contains="Query")
        self.assertEqual(studios.count(), 2)
        self.assertNotEqual(studios.count(), 0)


class GenreModelTestCase(TestCase):
    """Test cases for Genre model."""

    def setUp(self):
        self.genre = Genre.objects.create(
            name="Genre Name"
        )

    def test_creation(self):
        """Test creation of a Genre instance."""
        self.assertEqual(self.genre.name, "Genre Name")

    def test_unique_name(self):
        """Test that a Genre with a duplicate name cannot be created."""
        with self.assertRaises(IntegrityError):
            Genre.objects.create(name="Genre Name")

    def test_str_method(self):
        """Test srt method."""
        genre = Genre.objects.get(name="Genre Name")
        self.assertEqual(str(genre), "Genre Name")

    def test_query(self):
        """Test querying for Genre objects."""
        Genre.objects.create(
            name="Query Example One"
        )
        Genre.objects.create(
            name="Query Example Two"
        )
        genres = Genre.objects.filter(name__contains="Query")
        self.assertEqual(genres.count(), 2)
        self.assertNotEqual(genres.count(), 0)