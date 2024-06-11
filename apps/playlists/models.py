"""Models for Playlists App."""

from django.conf import settings
from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext as _

from apps.utils.models import BaseModel
from apps.utils.validators import FileSizeValidator, ImageSizeValidator
from apps.utils.paths import image_path
from apps.animes.models import Anime
from apps.mangas.models import Manga
from .choices import (
    ScoreChoices,
    PriorityChoices,
    StorageChoices,
    AnimeStatusChoices,
    MangaStatusChoices,
)

User = settings.AUTH_USER_MODEL


# TODO: Add PlaylistItemBase model


class PlaylistBase(BaseModel):
    """Model definition for Playlist (Base)."""

    # TODO: Update and migrate
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        db_index=True,
        verbose_name=_("user"),
    )
    banner = models.ImageField(
        _("banner"),
        upload_to=image_path,
        blank=True,
        null=True,
        validators=[
            FileExtensionValidator(allowed_extensions=["jpg", "webp"]),
            ImageSizeValidator(max_width=500, max_height=1500),
            FileSizeValidator(limit_mb=1),
        ],
    )
    is_public = models.BooleanField(_("is public"), default=True)

    # privacy choices

    class Meta:
        ordering = ["pk"]
        abstract = True


class AnimeList(PlaylistBase):
    """Model definition for AnimeList."""

    class Meta:
        verbose_name = _("animelist")
        verbose_name_plural = _("animelist")

    def __str__(self):
        return str(self.user)


class MangaList(PlaylistBase):
    """Model definition for MangaList."""

    class Meta:
        verbose_name = _("mangalist")
        verbose_name_plural = _("mangalist")

    def __str__(self):
        return str(self.user)


class AnimeListItem(BaseModel):
    """Model definition for AnimeListItem."""

    animelist_id = models.ForeignKey(
        AnimeList,
        on_delete=models.CASCADE,
        db_index=True,
        limit_choices_to={"is_available": True},
        verbose_name=_("animelist"),
    )
    anime_id = models.ForeignKey(
        Anime,
        on_delete=models.CASCADE,
        limit_choices_to={"is_available": True},
        verbose_name=_("anime"),
    )
    status = models.CharField(
        _("status"),
        max_length=20,
        choices=AnimeStatusChoices.choices,
        default=AnimeStatusChoices.PLAN_WATCH,
        db_index=True,
    )
    episodes_watched = models.PositiveIntegerField(_("episodes watched"), default=0)
    score = models.IntegerField(
        _("score"),
        choices=ScoreChoices.choices,
        blank=True,
        null=True,
    )
    start_date = models.DateField(_("start date"), blank=True, null=True)
    finish_date = models.DateField(_("finish date"), blank=True, null=True)
    tags = models.JSONField(
        _("tags"),
        blank=True,
        null=True,
        default=list,
    )
    priority = models.CharField(
        _("priority"),
        max_length=10,
        choices=PriorityChoices.choices,
        blank=True,
        null=True,
    )
    storage = models.CharField(
        _("storage"),
        max_length=10,
        choices=StorageChoices.choices,
        blank=True,
        null=True,
    )
    times_rewatched = models.PositiveIntegerField(_("times rewatched"), default=0)
    notes = models.TextField(_("notes"), blank=True)
    order = models.PositiveIntegerField(default=0)
    is_watched = models.BooleanField(_("is watched"), default=False, db_index=True)
    is_favorite = models.BooleanField(_("is favorite"), default=False, db_index=True)

    class Meta:
        ordering = ["pk"]
        verbose_name = _("animelist item")
        verbose_name_plural = _("animelist items")
        constraints = [
            models.UniqueConstraint(
                fields=["animelist_id", "anime_id"], name="unique_animelist_anime"
            )
        ]

    def __str__(self):
        return str(f"{self.animelist_id} - {self.anime_id}")


class MangaListItem(BaseModel):
    """Model definition for MangaListItem."""

    mangalist_id = models.ForeignKey(
        MangaList,
        on_delete=models.CASCADE,
        db_index=True,
        limit_choices_to={"is_available": True},
        verbose_name=_("mangalist"),
    )
    manga_id = models.ForeignKey(
        Manga,
        on_delete=models.CASCADE,
        limit_choices_to={"is_available": True},
        verbose_name=_("anime"),
    )
    status = models.CharField(
        _("status"),
        max_length=20,
        choices=MangaStatusChoices.choices,
        default=MangaStatusChoices.PLAN_READ,
        db_index=True,
    )
    volumes_read = models.PositiveIntegerField(_("volumes read"), default=0)
    chapters_read = models.PositiveIntegerField(_("chapters read"), default=0)
    score = models.IntegerField(
        _("score"),
        choices=ScoreChoices.choices,
        blank=True,
        null=True,
    )
    start_date = models.DateField(_("start date"), blank=True, null=True)
    finish_date = models.DateField(_("finish date"), blank=True, null=True)
    tags = models.JSONField(
        _("tags"),
        blank=True,
        null=True,
        default=list,
    )
    priority = models.CharField(
        _("priority"),
        max_length=10,
        choices=PriorityChoices.choices,
        blank=True,
        null=True,
    )
    storage = models.CharField(
        _("storage"),
        max_length=10,
        choices=StorageChoices.choices,
        blank=True,
        null=True,
    )
    times_reread = models.PositiveIntegerField(_("times re-read"), default=0)
    notes = models.TextField(_("notes"), blank=True)
    order = models.PositiveIntegerField(default=0)
    is_read = models.BooleanField(_("is read"), default=False, db_index=True)
    is_favorite = models.BooleanField(_("is favorite"), default=False, db_index=True)

    class Meta:
        ordering = ["pk"]
        verbose_name = _("mangalist item")
        verbose_name_plural = _("mangalist items")
        constraints = [
            models.UniqueConstraint(
                fields=["mangalist_id", "manga_id"], name="unique_mangalist_manga"
            )
        ]

    def __str__(self):
        return str(f"{self.mangalist_id} - {self.manga_id}")
