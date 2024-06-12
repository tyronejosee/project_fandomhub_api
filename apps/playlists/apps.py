"""Configs for Playlists App."""

from django.apps import AppConfig


class PlaylistsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.playlists"

    def ready(self):
        import apps.playlists.signals
