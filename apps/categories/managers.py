"""Managers for Categories App."""

from django.db.models import Manager


class StudioManager(Manager):
    """Manager for Studio model."""

    def get_available(self):
        return self.filter(available=True)


class GenreManager(Manager):
    """Manager for Genre model."""

    def get_available(self):
        return self.filter(available=True)


class ThemeManager(Manager):
    """Manager for Theme model."""

    def get_available(self):
        return self.filter(available=True)


class DemographicManager(Manager):
    """Manager for Season model."""

    def get_available(self):
        return self.filter(available=True)
