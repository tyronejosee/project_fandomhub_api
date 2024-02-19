"""Models for Watchlists App."""

from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _
from apps.contents.models import Anime, Manga
from apps.watchlists.choices import STATUS_CHOICES


User = settings.AUTH_USER_MODEL


class WatchlistBaseModel(models.Model):
    """Model definition for WatchlistBaseModel (Base)."""
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, db_index=True, verbose_name=_("User")
    )
    status = models.CharField(
        _("Status"), max_length=20, choices=STATUS_CHOICES, default=0,
        db_index=True
    )
    is_watched = models.BooleanField(
        _("Is Watched"), default=False, db_index=True
    )
    score = models.IntegerField(_("Score"), default=0)  # 10
    priority = models.IntegerField(_("Priority"), default=0)
    tags = models.CharField(_("Tags"), max_length=255, blank=True)
    comments = models.TextField(_("Comments"), blank=True)

    class Meta:
        """Meta definition for WatchlistItem."""
        abstract = True

    def __str__(self):
        return str(self.user)


class AnimeWatchlist(WatchlistBaseModel):
    """Model definition for AnimeWatchlist (Association)."""
    anime = models.ForeignKey(
        Anime, on_delete=models.CASCADE, verbose_name=_("Anime")
    )

    class Meta:
        """Meta definition for AnimeWatchlist."""
        verbose_name = _("AnimeWatchlist")
        verbose_name_plural = _("AnimeWatchlists")


class MangaWatchlist(WatchlistBaseModel):
    """Model definition for MangaWatchlist (Association)."""
    manga = models.ForeignKey(
        Manga, on_delete=models.CASCADE, verbose_name=_("Manga")
    )

    class Meta:
        """Meta definition for MangaWatchlist."""
        verbose_name = _("MangaWatchlist")
        verbose_name_plural = _("MangaWatchlists")
