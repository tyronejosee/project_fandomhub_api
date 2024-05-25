"""Models for Playlists App."""

from django.conf import settings
from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext as _

from apps.utils.models import BaseModel
from apps.utils.validators import FileSizeValidator, ImageSizeValidator
from apps.utils.paths import image_path
from apps.contents.models import Anime, Manga
from .managers import PlaylistManager, PlaylistBaseManager
from .choices import STATUS_CHOICES

User = settings.AUTH_USER_MODEL


class Tag(BaseModel):
    """Model definition for Tag."""

    name = models.CharField(_("name"), max_length=100)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, db_index=True, verbose_name=_("user")
    )

    class Meta:
        ordering = ["pk"]
        verbose_name = _("tag")
        verbose_name_plural = _("tags")

    def __str__(self):
        return str(f"{self.user} - {self.name}")


class Playlist(BaseModel):
    """Model definition for Playlist."""

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, db_index=True, verbose_name=_("user")
    )
    name = models.CharField(_("name"), max_length=100, unique=True)
    description = models.TextField(_("description"), blank=True, null=True)
    tags = models.ManyToManyField("Tag", verbose_name=_("tags"), blank=True)
    number_items = models.IntegerField(_("number of items"), default=0)
    cover = models.ImageField(
        _("image"),
        upload_to=image_path,
        blank=True,
        null=True,
        validators=[
            FileExtensionValidator(allowed_extensions=["jpg", "png", "webp"]),
            ImageSizeValidator(max_width=600, max_height=600),
            FileSizeValidator(limit_mb=1),
        ],
    )
    is_public = models.BooleanField(_("is public"), default=True)

    objects = PlaylistManager()

    # TODO: Add number_item logic

    class Meta:
        ordering = ["pk"]
        verbose_name = _("playlist")
        verbose_name_plural = _("playlists")

    def __str__(self):
        return str(f"{self.user} - {self.name}")


class PlaylistBase(BaseModel):
    """Model definition for PlaylistBase (Base)."""

    playlist = models.ForeignKey(
        Playlist, on_delete=models.CASCADE, db_index=True, verbose_name=_("playlist")
    )
    status = models.CharField(
        _("status"),
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending",
        db_index=True,
    )
    is_watched = models.BooleanField(_("is watched"), default=False, db_index=True)
    is_favorite = models.BooleanField(_("is favorite"), default=False, db_index=True)
    order = models.FloatField(default=0)

    objects = PlaylistBaseManager()

    class Meta:
        abstract = True


class PlaylistAnime(PlaylistBase):
    """Model definition for PlaylistAnime."""

    anime = models.ForeignKey(
        Anime,
        on_delete=models.CASCADE,
        related_name="playlist_anime",
        verbose_name=_("anime"),
    )

    class Meta:
        ordering = ["pk"]
        verbose_name = _("playlist anime")
        verbose_name_plural = _("playlist animes")

    def __str__(self):
        return str(f"{self.anime.name}")


class PlaylistManga(PlaylistBase):
    """Model definition for PlaylistManga."""

    manga = models.ForeignKey(
        Manga,
        on_delete=models.CASCADE,
        related_name="playlist_manga",
        verbose_name=_("manga"),
    )

    class Meta:
        ordering = ["pk"]
        verbose_name = _("playlist manga")
        verbose_name_plural = _("playlist mangas")

    def __str__(self):
        return str(f"{self.manga.name}")
