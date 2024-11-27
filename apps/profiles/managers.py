"""Managers for Profiles App."""

from apps.utils.managers import BaseManager


class ProfileManager(BaseManager):
    """Manager for Profile model."""

    def get_by_user(self, user):
        return self.get_available().get(user_id=user)
