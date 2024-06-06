"""Models for Animes App."""

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext as _

from apps.utils.paths import picture_image_path
from apps.utils.models import BaseModel
from apps.utils.mixins import SlugMixin
from apps.utils.validators import FileSizeValidator, ImageSizeValidator
from apps.categories.models import Theme
from apps.studios.models import Studio
from apps.genres.models import Genre
from apps.seasons.models import Season
from .managers import AnimeManager
from .choices import StatusChoices, MediaTypeChoices, RatingChoices, SourceChoices


class Anime(BaseModel, SlugMixin):
    """Model definition for Anime."""

    name = models.CharField(_("name (eng)"), max_length=255, unique=True)
    name_jpn = models.CharField(_("name (jpn)"), max_length=255, unique=True)
    name_rom = models.CharField(
        _("name (rmj)"), max_length=255, unique=True, blank=True
    )
    alternative_names = models.JSONField(
        _("alternative names"),
        blank=True,
        null=True,
        default=list,
    )
    image = models.ImageField(
        _("image"),
        upload_to=picture_image_path,
        blank=True,
        null=True,
        validators=[
            FileExtensionValidator(allowed_extensions=["jpg", "webp"]),
            ImageSizeValidator(max_width=909, max_height=1280),
            FileSizeValidator(limit_mb=2),
        ],
    )
    trailer = models.URLField(_("trailer"), max_length=255, blank=True)
    synopsis = models.TextField(_("synopsis"), blank=True, null=True)
    media_type = models.CharField(
        _("media type"),
        max_length=10,
        choices=MediaTypeChoices.choices,
        default=MediaTypeChoices.TV,
    )
    episodes = models.IntegerField(
        _("episodes"),
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(1500)],
    )
    status = models.CharField(
        _("status"),
        max_length=10,
        choices=StatusChoices.choices,
        default=StatusChoices.AIRING,
    )
    release = models.DateField(_("release"))
    season_id = models.ForeignKey(
        Season, on_delete=models.CASCADE, verbose_name=_("season")
    )  # Revition
    # premiered
    # broadcast
    # producers
    # licensors
    studio_id = models.ForeignKey(
        Studio,
        on_delete=models.CASCADE,
        verbose_name=_("studio"),
    )
    source = models.CharField(
        _("rating"),
        max_length=10,
        choices=SourceChoices.choices,
        default=SourceChoices.MANGA,
    )
    genres_id = models.ManyToManyField(Genre, verbose_name=_("genres"))
    themes_id = models.ManyToManyField(Theme, verbose_name=_("themes"))
    duration = models.CharField(_("duration"), max_length=20, blank=True)
    rating = models.CharField(
        _("rating"),
        max_length=10,
        choices=RatingChoices.choices,
        default=RatingChoices.PG13,
    )
    website = models.URLField(_("website"), max_length=255, blank=True)
    is_recommended = models.BooleanField(_("is recommended"), default=False)

    score = models.FloatField(_("mean"), blank=True, null=True)
    ranked = models.PositiveIntegerField(_("ranked"), default=0)
    popularity = models.PositiveIntegerField(_("popularity"), default=0)
    members = models.PositiveIntegerField(_("members"), default=0)
    favorites = models.PositiveIntegerField(_("favorites"), default=0)

    # is_publishing = models.BooleanField(_("is recommended"), default=False)

    objects = AnimeManager()

    class Meta:
        ordering = ["pk"]
        verbose_name = _("anime")
        verbose_name_plural = _("animes")

    def save(self, *args, **kwargs):
        if not self.name_rom:
            self.name_rom = self.name
        super(SlugMixin, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.name)


class AnimeStats(BaseModel):
    """Model definition for AnimeStats."""

    anime_id = models.OneToOneField(
        Anime,
        on_delete=models.CASCADE,
        related_name="stats",
    )
    watching = models.PositiveIntegerField(default=0)
    completed = models.PositiveIntegerField(default=0)
    on_hold = models.PositiveIntegerField(default=0)
    dropped = models.PositiveIntegerField(default=0)
    plan_to_watch = models.PositiveIntegerField(default=0)
    total = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["pk"]
        verbose_name = _("anime stats")
        verbose_name_plural = _("anime stats")

    def save(self, *args, **kwargs):
        # Overridden the method to calculate the total
        self.total = (
            self.watching
            + self.completed
            + self.on_hold
            + self.dropped
            + self.plan_to_watch
        )
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Stats for {self.anime_id}"
