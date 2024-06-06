"""Managers for Playlists App."""

from django.db.models import Manager


class PlaylistManager(Manager):
    """Manager for Playlist model."""

    def get_available(self):
        return self.filter(is_available=True)
