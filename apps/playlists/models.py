"""Models for Playlists App."""

from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _

from apps.utils.models import BaseModel
from apps.contents.models import Anime, Manga
from .choices import STATUS_CHOICES

User = settings.AUTH_USER_MODEL


class Playlist(BaseModel):
    """Model definition for Playlist (Entity)."""
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, db_index=True, verbose_name=_("user")
    )
    name = models.CharField(_("name"), max_length=255)

    class Meta:
        """Meta definition for Playlist."""
        verbose_name = _("playlist")
        verbose_name_plural = _("playlists")

    def __str__(self):
        return str(f"{self.user}'s playlist")


class PlaylistBase(BaseModel):
    """Model definition for PlaylistBase (Base)."""
    playlist = models.ForeignKey(
        Playlist, on_delete=models.CASCADE,
        db_index=True, verbose_name=_("playlist")
    )
    status = models.CharField(
        _("status"), max_length=20, choices=STATUS_CHOICES,
        default="pending", db_index=True
    )
    is_watched = models.BooleanField(
        _("is watched"), default=False, db_index=True
    )
    is_favorite = models.BooleanField(
        _("is favorite"), default=False, db_index=True
    )
    # order = models.IntegerField(default=0, db_index=True)

    class Meta:
        """Meta definition for PlaylistBase."""
        abstract = True


class PlaylistAnime(PlaylistBase):
    """Model definition for PlaylistAnime (Pivot)."""
    anime = models.ForeignKey(
        Anime, on_delete=models.CASCADE,
        related_name="playlist_animes", verbose_name=_("anime")
    )

    class Meta:
        """Meta definition for PlaylistAnime."""
        verbose_name = _("playlist anime")
        verbose_name_plural = _("playlist animes")

    def __str__(self):
        return str(f"{self.anime.name}")


class PlaylistManga(PlaylistBase):
    """Model definition for PlaylistManga (Pivot)."""
    manga = models.ForeignKey(
        Manga, on_delete=models.CASCADE,
        related_name="playlist_mangas", verbose_name=_("manga")
    )

    class Meta:
        """Meta definition for PlaylistManga."""
        verbose_name = _("playlist manga")
        verbose_name_plural = _("playlist mangas")

    def __str__(self):
        return str(f"{self.manga.name}")
