"""Managers for News App."""

from django.db.models import Manager


class NewsManager(Manager):
    """Manager for News model."""

    def get_available(self):
        return self.filter(available=True)
