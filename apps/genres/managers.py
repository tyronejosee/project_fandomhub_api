"""Managers for Genres App."""

from django.db.models import Manager


class GenreManager(Manager):
    """Manager for Genre model."""

    def get_available(self):
        return self.filter(is_available=True)


class ThemeManager(Manager):
    """Manager for Theme model."""

    def get_available(self):
        return self.filter(is_available=True)


class DemographicManager(Manager):
    """Manager for Season model."""

    def get_available(self):
        return self.filter(is_available=True)
