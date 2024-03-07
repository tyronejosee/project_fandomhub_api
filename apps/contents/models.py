"""Models for Contents App."""

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext as _
from apps.categories.models import Studio, Genre, Theme, Season, Demographic
from apps.utils.paths import image_path
from apps.utils.models import BaseModel
from apps.utils.mixins import SlugMixin
from apps.contents.choices import (
    STATUS_CHOICES, CATEGORY_CHOICES, RATING_CHOICES, MEDIA_TYPE_CHOICES
)
from apps.persons.models import Author


class Anime(BaseModel, SlugMixin):
    """Model definition for Anime (Entity)."""
    name = models.CharField(
        _("Name (English)"), max_length=255, unique=True, db_index=True
    )
    name_jpn = models.CharField(
        _("Name (Japanese)"), max_length=255, unique=True,
    )
    name_rom = models.CharField(
        _("Name (Romaji)"), max_length=255, unique=True, blank=True
    )
    image = models.ImageField(
        _("Image"), upload_to=image_path, blank=True, null=True
    )
    synopsis = models.TextField(_("Synopsis"), blank=True, null=True)
    episodes = models.IntegerField(
        _("Episodes"), default=0,
        validators=[MinValueValidator(0), MaxValueValidator(1500)]
    )
    duration = models.CharField(
        _("Duration"), max_length=20, blank=True, null=True
    )
    release = models.DateField(_("Release"), blank=True, null=True)
    category = models.IntegerField(
        _("Category"), choices=CATEGORY_CHOICES, default=0
    )
    website = models.URLField(max_length=255, blank=True)
    trailer = models.URLField(max_length=255, blank=True)
    status = models.IntegerField(
        _("Status"), choices=STATUS_CHOICES, default=0
    )
    rating = models.IntegerField(
        _("Rating"), choices=RATING_CHOICES, default=0
    )
    studio = models.ForeignKey(
        Studio, on_delete=models.CASCADE, blank=True, null=True
    )
    genres = models.ManyToManyField(Genre, blank=True)
    themes = models.ManyToManyField(Theme, blank=True)
    season = models.ForeignKey(
        Season, on_delete=models.CASCADE, blank=True, null=True
    )
    mean = models.FloatField(_("Mean"), blank=True, null=True)
    rank = models.IntegerField(_("Rank"), blank=True, null=True)
    popularity = models.IntegerField(_("Popularity"), blank=True, null=True)
    num_list_users = models.IntegerField(
        _("Number of List Users"), blank=True, null=True
    )
    num_scoring_users = models.IntegerField(
        _("Number of Scoring Users"), blank=True, null=True
    )

    class Meta:
        """Meta definition for Anime."""
        verbose_name = _("Anime")
        verbose_name_plural = _("Animes")

    def save(self, *args, **kwargs):
        if not self.name_rom or self.name_rom != self.name:
            self.name_rom = self.name
        super(SlugMixin, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.name)


class Manga(BaseModel, SlugMixin):
    """Model definition for Manga (Entity)."""
    name = models.CharField(
        _("Name (ENG)"), max_length=255, unique=True, db_index=True
    )
    name_jpn = models.CharField(_("Name (JPN)"), max_length=255, unique=True)
    name_rom = models.CharField(
        _("Name (Romaji)"), max_length=255, unique=True, blank=True
    )
    image = models.ImageField(
        _("Image"), upload_to=image_path, blank=True, null=True
    )
    synopsis = models.TextField(_("Synopsis"), blank=True, null=True)
    chapters = models.IntegerField(
        _("Chapters"), validators=[MinValueValidator(0)]
    )
    release = models.DateField(_("Release"), blank=True, null=True)
    media_type = models.IntegerField(
        _("Media Type"), choices=MEDIA_TYPE_CHOICES, default=0
    )
    website = models.URLField(max_length=255, blank=True)
    status = models.IntegerField(
        _("Status"), choices=STATUS_CHOICES, default=0
    )
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, blank=True, null=True
    )
    demographic = models.ForeignKey(
        Demographic, on_delete=models.CASCADE, blank=True, null=True
    )
    genres = models.ManyToManyField(Genre, blank=True)
    themes = models.ManyToManyField(Theme, blank=True)
    mean = models.FloatField(_("Mean"), blank=True, null=True)
    rank = models.IntegerField(_("Rank"), blank=True, null=True)
    popularity = models.IntegerField(_("Popularity"), blank=True, null=True)
    num_list_users = models.IntegerField(
        _("Number of List Users"), blank=True, null=True
    )
    num_scoring_users = models.IntegerField(
        _("Number of Scoring Users"), blank=True, null=True
    )

    class Meta:
        """Meta definition for Manga."""
        verbose_name = _("Manga")
        verbose_name_plural = _("Mangas")

    def save(self, *args, **kwargs):
        if not self.name_rom or self.name_rom != self.name:
            self.name_rom = self.name
            print(self.name_rom)
        super(SlugMixin, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.name)
