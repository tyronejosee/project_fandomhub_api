"""Managers for Profiles App."""

from django.db.models import Manager


class ProfileManager(Manager):
    """Manager for Profile model."""

    def get_available(self):
        return self.filter(is_available=True)

    def get_by_user(self, user):
        return self.get_available().get(user=user)
