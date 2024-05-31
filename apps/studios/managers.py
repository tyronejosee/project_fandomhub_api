"""Managers for Studios App."""

from django.db.models import Manager


class StudioManager(Manager):
    """Manager for Studio model."""

    def get_available(self):
        return self.filter(available=True)
