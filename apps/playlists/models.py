"""Models for Playlists App."""

from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _
from django.core.validators import MinValueValidator, MaxValueValidator
from apps.contents.models import Anime, Manga
from apps.playlists.choices import STATUS_CHOICES

User = settings.AUTH_USER_MODEL


class Playlist(models.Model):
    """Pending."""

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, db_index=True, verbose_name=_("User")
    )
    name = models.CharField(max_length=255)
    animes = models.ManyToManyField(Anime, through="PlaylistAnime")

    class Meta:
        """Meta definition for Playlist."""
        verbose_name = _("Playlist")
        verbose_name_plural = _("Playlists")

    def __str__(self):
        return str(self.user)


class PlaylistAnime(models.Model):
    """Pending."""

    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        default=0, validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    status = models.CharField(
        _("Status"), max_length=20, choices=STATUS_CHOICES,
        default="pending", db_index=True
    )
    is_watched = models.BooleanField(
        _("Is Watched"), default=False, db_index=True
    )
    score = models.IntegerField(_("Score"), default=0)  # 10
    priority = models.IntegerField(_("Priority"), default=0)
    tags = models.CharField(_("Tags"), max_length=255, blank=True)
    comments = models.TextField(_("Comments"), blank=True)

    class Meta:
        """Meta definition for PlaylistAnime."""
        verbose_name = _("PlaylistAnime")
        verbose_name_plural = _("PlaylistAnime")

    def __str__(self):
        return str(f"{self.playlist} - {self.anime}")


class PlaylistManga(models.Model):
    """Pending."""

    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        default=0, validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    status = models.CharField(
        _("Status"), max_length=20, choices=STATUS_CHOICES,
        default="pending", db_index=True
    )
    is_watched = models.BooleanField(
        _("Is Watched"), default=False, db_index=True
    )
    score = models.IntegerField(_("Score"), default=0)  # 10
    priority = models.IntegerField(_("Priority"), default=0)
    tags = models.CharField(_("Tags"), max_length=255, blank=True)
    comments = models.TextField(_("Comments"), blank=True)

    class Meta:
        """Meta definition for PlaylistManga."""
        verbose_name = _("PlaylistManga")
        verbose_name_plural = _("PlaylistManga")

    def __str__(self):
        return str(f"{self.playlist} - {self.manga}")
