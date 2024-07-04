"""Managers for Utils App."""

from django.db import models


class BaseManager(models.Manager):
    """Base Manager."""

    def get_available(self):
        return self.filter(is_available=True)

    def get_unavailable(self):
        return self.filter(is_available=False)


class PictureManager(BaseManager):
    """Manager for Picture model."""

    def get_character_pictures(self, character):
        return self.filter(
            content_type__model="character",
            object_id=character.id,
        )


class VideoManager(BaseManager):
    """Manager for Video model."""
