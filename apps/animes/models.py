"""Models for Animes App."""

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext as _

from apps.utils.paths import picture_image_path
from apps.utils.models import BaseModel
from apps.utils.mixins import SlugMixin
from apps.utils.validators import FileSizeValidator, ImageSizeValidator
from apps.producers.models import Producer
from apps.producers.choices import TypeChoices
from apps.genres.models import Genre, Theme
from .managers import AnimeManager
from .choices import (
    DayChoices,
    TimezoneChoices,
    StatusChoices,
    MediaTypeChoices,
    RatingChoices,
    SourceChoices,
    SeasonChoices,
)


class Broadcast(BaseModel):
    """Model definition for Broadcast."""

    string = models.CharField(_("string"), max_length=50, blank=True)
    day = models.CharField(
        _("day"),
        max_length=10,
        choices=DayChoices.choices,
    )
    time = models.TimeField(_("time"))
    timezone = models.CharField(
        _("timezone"),
        max_length=3,
        choices=TimezoneChoices.choices,
        default=TimezoneChoices.JST,
    )

    class Meta:
        ordering = ["pk"]
        verbose_name = _("broadcast")
        verbose_name_plural = _("broadcasts")

    def save(self, *args, **kwargs):
        # Automatically generate the string field
        self.string = f"{self.get_day_display()} at {self.time.strftime('%H:%M')} ({self.get_timezone_display()})"
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.string)


class Anime(BaseModel, SlugMixin):
    """Model definition for Anime."""

    name = models.CharField(_("name (eng)"), max_length=255, unique=True)
    name_jpn = models.CharField(_("name (jpn)"), max_length=255, unique=True)
    name_rom = models.CharField(
        _("name (rmj)"),
        max_length=255,
        unique=True,
        blank=True,
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
    background = models.TextField(_("background"), blank=True, null=True)
    season = models.CharField(
        _("season"),
        max_length=10,
        db_index=True,
        choices=SeasonChoices.choices,
    )
    year = models.IntegerField(
        _("year"),
        default=2010,
        db_index=True,
        validators=[MinValueValidator(1900), MaxValueValidator(2100)],
    )
    broadcast_id = models.ForeignKey(
        Broadcast,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        limit_choices_to={"is_available": True},
        verbose_name=_("broadcast"),
    )
    media_type = models.CharField(
        _("media type"),
        max_length=10,
        choices=MediaTypeChoices.choices,
        default=MediaTypeChoices.TV,
    )
    source = models.CharField(
        _("source"),
        max_length=10,
        choices=SourceChoices.choices,
        default=SourceChoices.MANGA,
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
    aired_from = models.DateField(_("aired from"))
    aired_to = models.DateField(_("aired to"), blank=True, null=True)
    producers = models.ManyToManyField(
        Producer,
        limit_choices_to={
            "type": TypeChoices.DISTRIBUTOR,
            "is_available": True,
        },
        related_name="produced_animes",
        verbose_name=_("producers"),
    )
    licensors_id = models.ForeignKey(
        Producer,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        limit_choices_to={
            "type": TypeChoices.LICENSOR,
            "is_available": True,
        },
        related_name="licensed_animes",
        verbose_name=_("licensors"),
    )
    studio_id = models.ForeignKey(
        Producer,
        on_delete=models.CASCADE,
        limit_choices_to={
            "type": TypeChoices.STUDIO,
            "is_available": True,
        },
        related_name="studio_animes",
        verbose_name=_("studio"),
    )
    genres = models.ManyToManyField(Genre, verbose_name=_("genres"))
    themes = models.ManyToManyField(Theme, verbose_name=_("themes"))
    duration = models.DurationField(_("duration"), blank=True)
    rating = models.CharField(
        _("rating"),
        max_length=10,
        choices=RatingChoices.choices,
        default=RatingChoices.PG13,
    )
    website = models.URLField(_("website"), max_length=255, blank=True)
    is_recommended = models.BooleanField(_("is recommended"), default=False)

    score = models.FloatField(_("score"), blank=True, null=True)
    ranked = models.PositiveIntegerField(_("ranked"), default=0)
    popularity = models.PositiveIntegerField(_("popularity"), default=0)
    members = models.PositiveIntegerField(_("members"), default=0)
    favorites = models.PositiveIntegerField(_("favorites"), default=0)

    # is_publishing = models.BooleanField(_("is_publishing"), default=False)
    # premiered = season + year
    # aired = aired_from / aired_to

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

    def calculate_score(self, user_score):
        # Calculate new score based on the existing score and the user's score
        if self.members >= 2:
            self.score = (self.score + user_score) / self.members
        else:
            self.score = user_score

    def calculate_ranked(self):
        # Calculate ranking of anime based on its score compared to all other animes
        all_animes = Anime.objects.all().order_by("-score")
        self.ranked = list(all_animes).index(self) + 1

    def calculate_popularity(self):
        # Calculate popularity of anime based on number of members who have it in list
        all_animes = Anime.objects.all().order_by("-members")
        self.popularity = list(all_animes).index(self) + 1


class AnimeStats(BaseModel):
    """Model definition for AnimeStats."""

    anime_id = models.OneToOneField(
        Anime,
        on_delete=models.CASCADE,
        related_name="stats",
        limit_choices_to={"is_available": True},
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
