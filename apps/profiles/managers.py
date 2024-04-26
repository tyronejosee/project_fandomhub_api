"""Managers for Profiles App."""

from django.db.models import Manager


class ProfileManager(Manager):
    """Manager for Profile model."""

    def get_queryset(self):
        # Default queryset
        return super().get_queryset()

    def get_available(self):
        """Get all available profiles"""
        return self.get_queryset().filter(available=True)

    def get_unavailable(self):
        """Get all unavailable profiles"""
        return self.get_queryset().filter(available=False)
