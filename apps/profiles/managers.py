"""Managers for Profiles App."""

from django.db.models import Manager


class ProfileManager(Manager):
    """Manager for Profile model."""

    def get_queryset(self):
        # Default queryset
        return super().get_queryset()

    def get_available(self):
        """Get all available profiles."""
        return self.get_queryset().filter(available=True)

    def get_by_user(self, user):
        """Get the profile for the specified user."""
        return self.get_available().get(user=user)
