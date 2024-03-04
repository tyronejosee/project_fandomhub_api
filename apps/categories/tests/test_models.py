"""Tests for Models in Categories App."""

from django.test import TestCase
from django.core.exceptions import ValidationError
from apps.categories.models import Studio, Genre, Season, Demographic


class StudioModelTestCase(TestCase):
    """Test cases for Studio model."""

    def test_valid_creation(self):
        """Test creation of a Studio instance."""
        studio = Studio.objects.create(
            name="Studio Ghibli",
            name_jpn="スタジオジブリ",
            established="Jun, 1985",
            image=None
        )
        self.assertEqual(studio.name, "Studio Ghibli")
        self.assertEqual(studio.name_jpn, "スタジオジブリ")
        self.assertEqual(studio.established, "Jun, 1985")
        self.assertEqual(studio.available, True)
        self.assertEqual(studio.image, None)

    def test_duplicate_studio_name(self):
        """Pending."""
        with self.assertRaises(ValidationError):
            studio1 = Studio(
                name="Studio Ghibli",
                name_jpn="スタジオジブリ"
            )
            studio1.save()

            studio2 = Studio(
                name="Studio Ghibli",
                name_jpn="Another Name"
            )
            studio2.full_clean()    # Error

    def test_update_studio(self):
        """Pending."""
        studio = Studio(name="MAPPA", name_jpn="MAPPA")
        studio.save()

        studio.name = "A-1 Pictures"
        studio.full_clean()
        studio.save()
        updated_studio = Studio.objects.get(pk=studio.pk)
        self.assertEqual(updated_studio.name, "A-1 Pictures")

    def test_delete_studio(self):
        """Pending."""
        studio = Studio(name="Bones", name_jpn="ボンズ")
        studio.save()
        studio.delete()
        with self.assertRaises(Studio.DoesNotExist):
            Studio.objects.get(pk=studio.pk)


class GenreModelTestCase(TestCase):
    """Test cases for Genre model."""

    def test_creation(self):
        """Test creation of a Genre instance."""
        genre = Genre.objects.create(
            name="Romance"
        )
        self.assertEqual(genre.name, "Romance")
        self.assertEqual(genre.available, True)

    def test_valid_genre(self):
        """Pending."""
        genre = Genre(name="Action")
        genre.full_clean()
        genre.save()

        saved_genre = Genre.objects.get(name="Action")
        self.assertEqual(saved_genre, genre)

    def test_duplicate_genre_name(self):
        """Pending."""
        with self.assertRaises(ValidationError):
            genre1 = Genre(name="Fantasy")
            genre1.save()

            genre2 = Genre(name="Fantasy")
            genre2.full_clean()    # Error

    def test_update_genre_name(self):
        """Pending."""
        genre = Genre(name="Drama")
        genre.save()

        genre.name = "Adventure"
        genre.full_clean()
        genre.save()

        updated_genre = Genre.objects.get(pk=genre.pk)
        self.assertEqual(updated_genre.name, "Adventure")
        self.assertNotEqual(updated_genre.name, "Drama")

    def test_delete_genre(self):
        """Pending."""
        genre = Genre(name='Action')
        genre.save()
        genre.delete()

        with self.assertRaises(Genre.DoesNotExist):
            Genre.objects.get(pk=genre.pk)


class SeasonModelTestCase(TestCase):
    """Test cases for Season model."""

    def test_creation(self):
        """Test creation of a Genre instance."""
        season = Season.objects.create(season=1, year=2024)
        self.assertEqual(season.season, 1)
        self.assertEqual(season.year, 2024)

    def test_valid_season(self):
        """Pending."""
        season = Season(season=1, year=2022)
        season.full_clean()
        season.save()

        saved_season = Season.objects.get(season=1, year=2022)
        self.assertEqual(saved_season, season)

    def test_invalid_season_value(self):
        """Pending."""
        with self.assertRaises(ValidationError):
            season = Season(season=5, year=2022)
            season.full_clean()    # Error

    def test_invalid_year_value(self):
        """Pending."""
        with self.assertRaises(ValidationError):
            season = Season(season=1, year=1899)    # Min=1900
            season.full_clean()

        with self.assertRaises(ValidationError):
            season = Season(season=1, year=2101)    # max=2100
            season.full_clean()

    def test_update_season(self):
        """Pending."""
        # Create
        season = Season(season=1, year=2022)
        season.save()

        # Update
        season.season = 2
        season.year = 2023
        season.full_clean()
        season.save()

        updated_season = Season.objects.get(pk=season.pk)
        self.assertEqual(updated_season.season, 2)
        self.assertEqual(updated_season.year, 2023)

    def test_delete_season(self):
        """Pending."""
        season = Season(season=1, year=2022)
        season.save()
        season.delete()
        with self.assertRaises(Season.DoesNotExist):
            Season.objects.get(pk=season.pk)


class DemographicModelTestCase(TestCase):
    """Test cases for Demographic model."""

    def test_valid_demographic(self):
        """Pending."""
        demographic = Demographic(name="Shoujo")
        demographic.full_clean()
        demographic.save()

        saved_demographic = Demographic.objects.get(name="Shoujo")
        self.assertEqual(saved_demographic, demographic)

    def test_duplicate_demographic_name(self):
        """Pending."""
        with self.assertRaises(ValidationError):
            demographic1 = Demographic(name="Seinen")
            demographic1.save()

            demographic2 = Demographic(name="Seinen")
            demographic2.full_clean()    # Error

    def test_update_demographic_name(self):
        """Pending."""
        demographic = Demographic(name="Josei")
        demographic.save()

        # Update
        demographic.name = "Seijin"
        demographic.full_clean()
        demographic.save()

        updated_demographic = Demographic.objects.get(pk=demographic.pk)
        self.assertEqual(updated_demographic.name, "Seijin")

    def test_delete_demographic(self):
        """Pending."""
        demographic = Demographic(name='Young Adults')
        demographic.save()

        # Remove
        demographic.delete()

        with self.assertRaises(Demographic.DoesNotExist):
            Demographic.objects.get(pk=demographic.pk)
