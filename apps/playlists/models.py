"""Models for Playlists App."""

from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _
from apps.utils.models import BaseModel
from apps.contents.models import Anime, Manga
from apps.playlists.choices import STATUS_CHOICES

User = settings.AUTH_USER_MODEL


class Playlist(BaseModel):
    """Model definition for Playlist (Entity)."""
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, db_index=True, verbose_name=_("User")
    )
    name = models.CharField(_("Name"), max_length=255)

    class Meta:
        """Meta definition for Playlist."""
        verbose_name = _("Playlist")
        verbose_name_plural = _("Playlists")

    def __str__(self):
        return str(f"{self.user}'s playlist")


class PlaylistBase(BaseModel):
    """Model definition for PlaylistBase (Base)."""
    playlist = models.ForeignKey(
        Playlist, on_delete=models.CASCADE,
        db_index=True, verbose_name=_("Playlist")
    )
    status = models.CharField(
        _("Status"),max_length=20, choices=STATUS_CHOICES,
        default="pending", db_index=True
    )
    is_watched = models.BooleanField(
        _("Is Watched"), default=False, db_index=True
    )
    is_favorite = models.BooleanField(
        _("Is Favorite"), default=False, db_index=True
    )
    # order = models.IntegerField(default=0, db_index=True)

    class Meta:
        """Meta definition for PlaylistBase."""
        abstract = True


class PlaylistAnime(PlaylistBase):
    """Model definition for PlaylistAnime (Pivot)."""
    anime = models.ForeignKey(
        Anime, on_delete=models.CASCADE,
        related_name="playlist_animes", verbose_name=_("Anime")
    )

    class Meta:
        """Meta definition for PlaylistAnime."""
        verbose_name = _("PlaylistAnime")
        verbose_name_plural = _("PlaylistAnimes")

    def __str__(self):
        return str(f"{self.anime.name}")


class PlaylistManga(PlaylistBase):
    """Model definition for PlaylistManga (Pivot)."""
    manga = models.ForeignKey(
        Manga, on_delete=models.CASCADE,
        related_name="playlist_mangas", verbose_name=_("Manga")
    )

    class Meta:
        """Meta definition for PlaylistManga."""
        verbose_name = _("PlaylistManga")
        verbose_name_plural = _("PlaylistMangas")

    def __str__(self):
        return str(f"{self.manga.name}")
