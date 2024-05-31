"""Managers for Categories App."""

from django.db.models import Manager


class ThemeManager(Manager):
    """Manager for Theme model."""

    def get_available(self):
        return self.filter(available=True)


class DemographicManager(Manager):
    """Manager for Season model."""

    def get_available(self):
        return self.filter(available=True)
