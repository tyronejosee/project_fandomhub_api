"""Managers for Categories App."""

from django.db.models import Manager


class SeasonManager(Manager):
    """Manager for Season model."""

    def get_available(self):
        return self.filter(available=True)
