"""Tests for Models in Seasons App."""

from django.test import TestCase
from django.core.exceptions import ValidationError

from ..models import Season


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
