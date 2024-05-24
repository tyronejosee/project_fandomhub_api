"""Managers for News App."""

from django.db.models import Manager


class NewManager(Manager):
    """Manager for New model."""

    def get_available(self):
        return self.filter(available=True)
