"""Managers for Playlists App."""

from django.db.models import Manager


class PlaylistManager(Manager):
    """Manager for Author model."""

    def get_available(self):
        return self.filter(available=True)


class PlaylistBaseManager(Manager):
    """Manager for PlaylistBase."""

    def get_available(self):
        return self.filter(available=True)
