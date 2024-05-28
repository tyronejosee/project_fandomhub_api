"""Tests for Models in Categories App."""

from django.test import TestCase
from django.core.exceptions import ValidationError

from apps.categories.models import Studio, Genre, Theme, Season, Demographic


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
        self.assertEqual(studio.available, True)
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

    def test_validate_name_field(self):
        """Test name field validation."""
        with self.assertRaises(ValidationError):
            genre1 = Genre(name="Fantasy")
            genre1.save()

            genre2 = Genre(name="Fantasy")
            genre2.full_clean()  # Error


class ThemeModelTestCase(TestCase):
    """Test cases for Theme model."""

    def test_creation_theme(self):
        """Test creating a theme."""
        theme = Theme.objects.create(name="Parody")
        self.assertEqual(theme.name, "Parody")
        self.assertEqual(theme.available, True)

    def test_update_theme(self):
        """Test updating a theme."""
        theme = Theme(name="Super Power")
        theme.save()

        theme.name = "Adult Cast"
        theme.full_clean()
        theme.save()

        updated_theme = Theme.objects.get(pk=theme.pk)
        self.assertEqual(updated_theme.name, "Adult Cast")
        self.assertNotEqual(updated_theme.name, "Super Power")

    def test_delete_theme(self):
        """Test deleting a theme."""
        theme = Theme(name="Isekai")
        theme.save()
        theme.delete()

        with self.assertRaises(Theme.DoesNotExist):
            Theme.objects.get(pk=theme.pk)

    def test_validate_name_field(self):
        """Test name field validation."""
        with self.assertRaises(ValidationError):
            theme1 = Theme(name="Fantasy")
            theme1.save()

            theme2 = Theme(name="Fantasy")
            theme2.full_clean()  # Error


class SeasonModelTestCase(TestCase):
    """Test cases for Season model."""

    def test_creation_season(self):
        """Test creating a season"""
        season = Season.objects.create(season="winter", year=2024)
        self.assertEqual(season.season, "winter")
        self.assertEqual(season.year, 2024)

    def test_update_season(self):
        """Test updating a season."""
        season = Season(season="winter", year=2022)
        season.save()

        season.season = "spring"
        season.year = 2023
        season.full_clean()
        season.save()

        updated_season = Season.objects.get(pk=season.pk)
        self.assertEqual(updated_season.season, "spring")
        self.assertEqual(updated_season.year, 2023)

    def test_delete_season(self):
        """Test deleting a season."""
        season = Season(season="summer", year=2022)
        season.save()
        season.delete()
        with self.assertRaises(Season.DoesNotExist):
            Season.objects.get(pk=season.pk)

    def test_validate_season_field(self):
        """Test season field validation."""
        with self.assertRaises(ValidationError):
            season = Season(season=5, year=2022)
            season.full_clean()  # Error

    def test_validate_year_field(self):
        """Test year field validation."""
        with self.assertRaises(ValidationError):
            season = Season(season=1, year=1899)  # Min=1900
            season.full_clean()

        with self.assertRaises(ValidationError):
            season = Season(season=1, year=2101)  # max=2100
            season.full_clean()


class DemographicModelTestCase(TestCase):
    """Test cases for Demographic model."""

    def test_creation_demographic(self):
        """Test creating a demographic."""
        demographic = Demographic(name="Shoujo")
        demographic.full_clean()
        demographic.save()

        saved_demographic = Demographic.objects.get(name="Shoujo")
        self.assertEqual(saved_demographic, demographic)

    def test_update_demographic(self):
        """Test updating a demographic."""
        demographic = Demographic(name="Josei")
        demographic.save()

        # Update
        demographic.name = "Seijin"
        demographic.full_clean()
        demographic.save()

        updated_demographic = Demographic.objects.get(pk=demographic.pk)
        self.assertEqual(updated_demographic.name, "Seijin")

    def test_delete_demographic(self):
        """Test deleting a demographic."""
        demographic = Demographic(name="Young Adults")
        demographic.save()

        demographic.delete()

        with self.assertRaises(Demographic.DoesNotExist):
            Demographic.objects.get(pk=demographic.pk)

    def test_validate_name_field(self):
        """Test name field validation."""
        with self.assertRaises(ValidationError):
            demographic1 = Demographic(name="Seinen")
            demographic1.save()

            demographic2 = Demographic(name="Seinen")
            demographic2.full_clean()  # Error
