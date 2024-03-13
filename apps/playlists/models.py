"""Models for Playlists App."""

from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _
from apps.contents.models import Anime, Manga
from apps.playlists.choices import STATUS_CHOICES

User = settings.AUTH_USER_MODEL


class Playlist(models.Model):
    """Model definition for Playlist (Entity)."""
    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, db_index=True, verbose_name=_("User")
    )
    created_at = models.DateTimeField(auto_now_add=True)
    anime_items = models.ManyToManyField(Anime, through="PlaylistItem")
    manga_items = models.ManyToManyField(Manga, through="PlaylistItem")

    class Meta:
        """Meta definition for Playlist."""
        verbose_name = _("Playlist")
        verbose_name_plural = _("Playlists")

    def __str__(self):
        return str(f"{self.user}'s playlist - {self.name}")


class PlaylistItem(models.Model):
    """Model definition for PlaylistItem (Pivot)."""
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    anime = models.ForeignKey(
        Anime, on_delete=models.CASCADE, null=True, blank=True)
    manga = models.ForeignKey(
        Manga, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES,
        default="pending", db_index=True
    )
    is_watched = models.BooleanField(default=False, db_index=True)

    class Meta:
        """Meta definition for PlaylistItem."""
        verbose_name = _("PlaylistItem")
        verbose_name_plural = _("PlaylistItems")

    def __str__(self):
        return str(f"{self.playlist} items")
