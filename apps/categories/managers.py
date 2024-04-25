"""Manager for Categories App."""

from django.db import models


class StudioManager(models.Manager):
    """Manager for Studio Model."""

    def get_queryset(self):
        # Default queryset
        return super().get_queryset()

    def get_available(self):
        return self.get_queryset().filter(available=True)


class GenreManager(models.Manager):
    """Manager for Genre Model."""

    def get_queryset(self):
        # Default queryset
        return super().get_queryset()

    def get_available(self):
        return self.get_queryset().filter(available=True)


class ThemeManager(models.Manager):
    """Manager for Theme Model."""

    def get_queryset(self):
        # Default queryset
        return super().get_queryset()

    def get_available(self):
        return self.get_queryset().filter(available=True)


class SeasonManager(models.Manager):
    """Manager for Season Model."""

    def get_queryset(self):
        # Default queryset
        return super().get_queryset()

    def get_available(self):
        return self.get_queryset().filter(available=True)


class DemographicManager(models.Manager):
    """Manager for Season Model."""

    def get_queryset(self):
        # Default queryset
        return super().get_queryset()

    def get_available(self):
        return self.get_queryset().filter(available=True)
