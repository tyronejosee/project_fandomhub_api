"""Models for Contents App."""

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext as _

from apps.utils.paths import image_path
from apps.utils.models import BaseModel
from apps.utils.mixins import SlugMixin
from apps.categories.models import Studio, Genre, Theme, Season, Demographic
from apps.persons.models import Author
from .choices import (
    STATUS_CHOICES, CATEGORY_CHOICES, RATING_CHOICES, MEDIA_TYPE_CHOICES
)


class Anime(BaseModel, SlugMixin):
    """Model definition for Anime (Entity)."""
    name = models.CharField(
        _("name (eng)"), max_length=255, unique=True, db_index=True
    )
    name_jpn = models.CharField(
        _("name (jpn)"), max_length=255, unique=True,
    )
    name_rom = models.CharField(
        _("name (rmj)"), max_length=255, unique=True, blank=True
    )
    image = models.ImageField(
        _("image"), upload_to=image_path, blank=True, null=True
    )
    synopsis = models.TextField(_("synopsis"), blank=True, null=True)
    episodes = models.IntegerField(
        _("episodes"), default=0,
        validators=[MinValueValidator(0), MaxValueValidator(1500)]
    )
    duration = models.CharField(
        _("duration"), max_length=20, blank=True, null=True
    )
    release = models.DateField(_("release"), blank=True, null=True)
    category = models.CharField(
        _("category"), max_length=10, choices=CATEGORY_CHOICES,
        default="pending"
    )
    website = models.URLField(max_length=255, blank=True)
    trailer = models.URLField(max_length=255, blank=True)
    status = models.CharField(
        _("status"), max_length=10, choices=STATUS_CHOICES, default="pending"
    )
    rating = models.CharField(
        _("rating"), max_length=10, choices=RATING_CHOICES, default="pending"
    )
    studio = models.ForeignKey(
        Studio, on_delete=models.CASCADE, blank=True, null=True
    )
    genres = models.ManyToManyField(Genre, blank=True)
    themes = models.ManyToManyField(Theme, blank=True)
    season = models.ForeignKey(
        Season, on_delete=models.CASCADE, blank=True, null=True
    )
    mean = models.FloatField(_("mean"), blank=True, null=True)
    rank = models.IntegerField(_("rank"), blank=True, null=True)
    popularity = models.IntegerField(_("popularity"), blank=True, null=True)
    favorites = models.IntegerField(
        _("favorites"), blank=True, null=True, default=0
    )
    num_list_users = models.IntegerField(
        _("number of list users"), blank=True, null=True, default=0
    )

    class Meta:
        """Meta definition for Anime."""
        verbose_name = _("anime")
        verbose_name_plural = _("animes")

    def save(self, *args, **kwargs):
        if not self.name_rom:
            self.name_rom = self.name
        super(SlugMixin, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.name)


class Manga(BaseModel, SlugMixin):
    """Model definition for Manga (Entity)."""
    name = models.CharField(
        _("name (eng)"), max_length=255, unique=True, db_index=True
    )
    name_jpn = models.CharField(_("name (jpn)"), max_length=255, unique=True)
    name_rom = models.CharField(
        _("name (rmj)"), max_length=255, unique=True, blank=True
    )
    image = models.ImageField(
        _("image"), upload_to=image_path, blank=True, null=True
    )
    synopsis = models.TextField(_("synopsis"), blank=True, null=True)
    chapters = models.IntegerField(
        _("chapters"), validators=[MinValueValidator(0)]
    )
    release = models.DateField(_("release"), blank=True, null=True)
    media_type = models.CharField(
        _("media type"), max_length=10, choices=MEDIA_TYPE_CHOICES,
        default="pending"
    )
    website = models.URLField(_("website"), max_length=255, blank=True)
    status = models.CharField(
        _("status"), max_length=10, choices=STATUS_CHOICES, default="pending"
    )
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, blank=True, null=True,
        verbose_name=_("author")
    )
    demographic = models.ForeignKey(
        Demographic, on_delete=models.CASCADE, blank=True, null=True,
        verbose_name=_("demographic")
    )
    genres = models.ManyToManyField(
        Genre, blank=True, verbose_name=_("genres")
    )
    themes = models.ManyToManyField(
        Theme, blank=True, verbose_name=_("themes")
    )
    mean = models.FloatField(_("mean"), blank=True, null=True)
    rank = models.IntegerField(_("rank"), blank=True, null=True)
    popularity = models.IntegerField(_("popularity"), blank=True, null=True)
    favorites = models.IntegerField(
        _("favorites"), blank=True, null=True, default=0
    )
    num_list_users = models.IntegerField(
        _("number of list users"), blank=True, null=True, default=0
    )

    class Meta:
        """Meta definition for Manga."""
        verbose_name = _("manga")
        verbose_name_plural = _("mangas")

    def save(self, *args, **kwargs):
        if not self.name_rom:
            self.name_rom = self.name
        super(SlugMixin, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.name)
