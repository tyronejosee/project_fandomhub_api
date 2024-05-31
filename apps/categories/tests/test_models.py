"""Tests for Models in Categories App."""

from django.test import TestCase
from django.core.exceptions import ValidationError

from ..models import Theme, Demographic


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
