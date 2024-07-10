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

    def get_anime_pictures(self, anime):
        return self.get_available().filter(
            content_type__model="anime",
            object_id=anime.id,
        )

    def get_manga_pictures(self, manga):
        return self.get_available().filter(
            content_type__model="manga",
            object_id=manga.id,
        )

    def get_character_pictures(self, character):
        return self.get_available().filter(
            content_type__model="character",
            object_id=character.id,
        )

    def get_person_pictures(self, person):
        return self.get_available().filter(
            content_type__model="person",
            object_id=person.id,
        )


class VideoManager(BaseManager):
    """Manager for Video model."""

    def get_anime_videos(self, anime):
        return self.get_available().filter(
            content_type__model="anime",
            object_id=anime.id,
        )
