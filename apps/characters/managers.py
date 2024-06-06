"""Managers for Characters App."""

from django.db.models import Manager


class CharacterManager(Manager):
    """Manager for Character model."""

    def get_available(self):
        return self.filter(is_available=True)
