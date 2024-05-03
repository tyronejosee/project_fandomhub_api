"""Managers for Persons App."""

from django.db.models import Manager


class AuthorManager(Manager):
    """Manager for Author model."""

    def get_queryset(self):
        # Default queryset
        return super().get_queryset()

    def get_available(self):
        """Get all available authors."""
        return self.get_queryset().filter(available=True)
