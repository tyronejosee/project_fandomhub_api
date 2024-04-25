"""Manager for Categories App."""

from django.db.models import Manager


class StudioManager(Manager):
    """Manager for Studio model."""

    def get_queryset(self):
        # Default queryset
        return super().get_queryset()

    def get_available(self):
        """Get all available studios"""
        return self.get_queryset().filter(available=True)


class GenreManager(Manager):
    """Manager for Genre model."""

    def get_queryset(self):
        # Default queryset
        return super().get_queryset()

    def get_available(self):
        """Get all available genres"""
        return self.get_queryset().filter(available=True)


class ThemeManager(Manager):
    """Manager for Theme model."""

    def get_queryset(self):
        # Default queryset
        return super().get_queryset()

    def get_available(self):
        """Get all available themes"""
        return self.get_queryset().filter(available=True)


class SeasonManager(Manager):
    """Manager for Season model."""

    def get_queryset(self):
        # Default queryset
        return super().get_queryset()

    def get_available(self):
        """Get all available seasons"""
        return self.get_queryset().filter(available=True)


class DemographicManager(Manager):
    """Manager for Season model."""

    def get_queryset(self):
        # Default queryset
        return super().get_queryset()

    def get_available(self):
        """Get all available demographics"""
        return self.get_queryset().filter(available=True)
