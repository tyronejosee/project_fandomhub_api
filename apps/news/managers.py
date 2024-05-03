"""Managers for News App."""

from django.db.models import Manager


class NewManager(Manager):
    """Manager for New model."""

    def get_queryset(self):
        # Default queryset
        return super().get_queryset()

    def get_available(self):
        """Get all available news"""
        return self.get_queryset().filter(available=True)
