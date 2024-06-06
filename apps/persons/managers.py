"""Managers for Persons App."""

from django.db.models import Manager


class PersonManager(Manager):
    """Manager for Person model."""

    def get_available(self):
        return self.filter(is_available=True)
