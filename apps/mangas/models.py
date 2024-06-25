"""Models for Mangas App."""

from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext as _

from apps.utils.paths import picture_image_path
from apps.utils.models import BaseModel
from apps.utils.mixins import SlugMixin
from apps.utils.validators import FileSizeValidator, ImageSizeValidator
from apps.genres.models import Genre, Theme, Demographic
from apps.persons.models import Person
from apps.persons.choices import CategoryChoices
from .managers import MangaManager, MagazineManager
from .choices import StatusChoices, MediaTypeChoices


class Magazine(BaseModel, SlugMixin):
    """Model definition for Magazine."""

    name = models.CharField(_("name"), max_length=255)
    count = models.PositiveIntegerField(_("count"), default=0)

    class Meta:
        ordering = ["pk"]
        verbose_name = _("magazine")
        verbose_name_plural = _("magazines")

    objects = MagazineManager()

    def __str__(self):
        return self.name


class Manga(BaseModel, SlugMixin):
    """Model definition for Manga."""

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
    synopsis = models.TextField(_("synopsis"), blank=True, null=True)
    background = models.TextField(_("background"), blank=True, null=True)
    media_type = models.CharField(
        _("media type"),
        max_length=10,
        choices=MediaTypeChoices.choices,
        default=MediaTypeChoices.MANGA,
    )
    chapters = models.PositiveIntegerField(_("chapters"), default=1)
    volumes = models.PositiveIntegerField(_("volumes"), default=1)
    status = models.CharField(
        _("status"),
        max_length=10,
        choices=StatusChoices.choices,
        default=StatusChoices.AIRING,
    )
    published_from = models.DateField(_("published from"))
    published_to = models.DateField(_("published to"), blank=True, null=True)
    genres = models.ManyToManyField(Genre, verbose_name=_("genres"))
    themes = models.ManyToManyField(Theme, verbose_name=_("themes"))
    demographic_id = models.ForeignKey(
        Demographic,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        limit_choices_to={"is_available": True},
        verbose_name=_("demographic"),
    )
    serialization_id = models.ForeignKey(
        Magazine,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name=_("serialization"),
    )
    author_id = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        limit_choices_to={
            "category": CategoryChoices.ARTIST,
            "is_available": True,
        },
        verbose_name=_("author"),
    )
    website = models.URLField(_("website"), max_length=255, blank=True)
    is_recommended = models.BooleanField(_("is recommended"), default=False)

    score = models.FloatField(_("score"), blank=True, null=True)
    ranked = models.PositiveIntegerField(_("ranked"), default=0)
    popularity = models.PositiveIntegerField(_("popularity"), default=0)
    members = models.PositiveIntegerField(_("members"), default=0)
    favorites = models.PositiveIntegerField(_("favorites"), default=0)

    # published = published_from / published_to

    objects = MangaManager()

    class Meta:
        ordering = ["pk"]
        verbose_name = _("manga")
        verbose_name_plural = _("mangas")

    def save(self, *args, **kwargs):
        if not self.name_rom:
            self.name_rom = self.name
        super(SlugMixin, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.name)

    def calculate_score(self, user_score):
        # Calculate score based on the existing score and the user's score
        if self.members >= 2:
            self.score = (self.score + user_score) / self.members
        else:
            self.score = user_score

    def calculate_ranked(self):
        # Calculate ranking of manga based on its score compared to all other mangas
        all_mangas = Manga.objects.all().order_by("-score")
        self.ranked = list(all_mangas).index(self) + 1

    def calculate_popularity(self):
        # Calculate popularity of manga based on number of members who have it in list
        all_mangas = Manga.objects.all().order_by("-members")
        self.popularity = list(all_mangas).index(self) + 1


class MangaStats(BaseModel):
    """Model definition for MangaStats."""

    manga_id = models.OneToOneField(
        Manga,
        on_delete=models.CASCADE,
        related_name="stats",
    )
    reading = models.PositiveIntegerField(default=0)
    completed = models.PositiveIntegerField(default=0)
    on_hold = models.PositiveIntegerField(default=0)
    dropped = models.PositiveIntegerField(default=0)
    plan_to_read = models.PositiveIntegerField(default=0)
    total = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["pk"]
        verbose_name = _("manga stats")
        verbose_name_plural = _("manga stats")

    def save(self, *args, **kwargs):
        # Overridden the method to calculate the total
        self.total = (
            self.reading
            + self.completed
            + self.on_hold
            + self.dropped
            + self.plan_to_read
        )
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Stats for {self.manga_id}"
