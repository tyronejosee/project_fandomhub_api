"""Managers for Persons App."""

from django.db.models import Manager


class AuthorManager(Manager):
    """Manager for Author model."""

    def get_available(self):
        return self.filter(available=True)
