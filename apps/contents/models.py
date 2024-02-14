"""Models for Contents App."""

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext as _
from apps.categories.models import Url, Studio, Genre, Season, Demographic
from apps.utils.paths import image_path
from apps.utils.models import BaseModel
from apps.utils.mixins import SlugMixin
from apps.contents.choices import (
    STATUS_CHOICES, CATEGORY_CHOICES, RATING_CHOICES, MEDIA_TYPE_CHOICES
)
from apps.persons.models import Author


class Anime(BaseModel, SlugMixin):
    """Model definition for Anime (Entity)."""
    name = models.CharField(_('Name (ENG)'), max_length=255, unique=True)
    name_jpn = models.CharField(_('Name (JPN)'), max_length=255, unique=True)
    image = models.ImageField(_('Image'), upload_to=image_path, blank=True, null=True)
    synopsis = models.TextField(_('Synopsis'), blank=True, null=True)
    episodes = models.IntegerField(
        _('Episodes'), validators=[MinValueValidator(0), MaxValueValidator(1500)], default=0
    )
    duration = models.CharField(_('Duration'), max_length=20, blank=True, null=True)
    release = models.DateField(_('Release'), blank=True, null=True)
    category = models.IntegerField(_('Category'), choices=CATEGORY_CHOICES, default=0)
    status = models.IntegerField(_('Status'), choices=STATUS_CHOICES, default=0)
    rating = models.IntegerField(_('Rating'), choices=RATING_CHOICES, default=0)
    studio_id = models.ForeignKey(Studio, on_delete=models.CASCADE, blank=True, null=True)
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE, blank=True, null=True)
    season_id = models.ForeignKey(Season, on_delete=models.CASCADE, blank=True, null=True)
    url_id = models.ManyToManyField(Url, blank=True)

    class Meta:
        """Meta definition for Anime."""
        verbose_name = _('Anime')
        verbose_name_plural = _('Animes')

    def __str__(self):
        return str(self.name)

    def get_image(self):
        """Returns the image URL or an empty string."""
        if self.image:
            return str(self.image.url)
        return ''


class Manga(BaseModel, SlugMixin):
    """Model definition for Manga (Entity)."""
    name = models.CharField(_('Name (ENG)'), max_length=255, unique=True)
    name_jpn = models.CharField(_('Name (JPN)'), max_length=255, unique=True)
    image = models.ImageField(_('Image'), upload_to=image_path, blank=True, null=True)
    synopsis = models.TextField(_('Synopsis'), blank=True, null=True)
    chapters = models.IntegerField(_('Chapters'), validators=[MinValueValidator(0)])
    release = models.DateField(_('Release'), blank=True, null=True)
    media_type = models.IntegerField(_('Media Type'), choices=MEDIA_TYPE_CHOICES, default=0)
    status = models.IntegerField(_('Status'), choices=STATUS_CHOICES, default=0)
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=True)
    demographic_id = models.ForeignKey(Demographic, on_delete=models.CASCADE, blank=True, null=True)
    genre_id = models.ManyToManyField(Genre, blank=True)
    url_id = models.ManyToManyField(Url, blank=True)

    class Meta:
        """Meta definition for Manga."""
        verbose_name = _('Manga')
        verbose_name_plural = _('Mangas')

    def __str__(self):
        return str(self.name)

    def get_image(self):
        """Returns the image URL or an empty string."""
        if self.image:
            return str(self.image.url)
        return ''
