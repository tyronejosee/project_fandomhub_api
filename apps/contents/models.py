"""Models for Contents App."""

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext as _
from apps.utils.models import BaseModel
from apps.utils.mixins import SlugMixin


class Url(BaseModel):
    """Model definition for Url (Association)."""
    TAG_CHOICES = [
        ('P', _('Pending')),
        ('S', _('Official Site')),
        ('C', _('Crunchyroll')),
        ('N', _('Netflix')),
        ('Y', _('Youtube Acccount')),
        ('X', _('X Account')),
    ]
    url = models.URLField(_('URL'))
    tag = models.CharField(_('Tag'), max_length=1, choices=TAG_CHOICES, default='P')

    class Meta:
        """Meta definition for Url."""
        verbose_name = _('Url')
        verbose_name_plural = _('Urls')

    def __str__(self):
        return str(self.url)


class Studio(BaseModel, SlugMixin):
    """Model definition for Studio (Catalog)."""
    name = models.CharField(_('Name (ENG)'), max_length=255, unique=True)
    name_jpn = models.CharField(_('Name (JPN)'), max_length=255, unique=True)
    established = models.CharField(_('Established'), max_length=255, blank=True, null=True)
    image = models.ImageField(_('Image'), upload_to='studios/')

    class Meta:
        """Meta definition for Studio."""
        verbose_name = _('Studio')
        verbose_name_plural = _('Studios')

    def __str__(self):
        return str(self.name)


class Genre(BaseModel, SlugMixin):
    """Model definition for Genre (Catalog)."""
    name = models.CharField(_('Name'), max_length=255, unique=True)

    class Meta:
        """Meta definition for Genre."""
        verbose_name = _('Genre')
        verbose_name_plural = _('Genres')

    def __str__(self):
        return str(self.name)


class Season(BaseModel, SlugMixin):
    """Model definition for Season (Catalog)."""
    name = models.CharField(_('Name'), max_length=25, unique=True)

    class Meta:
        """Meta definition for Season."""
        verbose_name = _('Season')
        verbose_name_plural = _('Season')

    def __str__(self):
        return str(self.name)


class Rating(BaseModel):
    """Model definition for Rating (Catalog)."""
    name = models.CharField(_('Name'), max_length=50, unique=True)

    class Meta:
        """Meta definition for Rating."""
        verbose_name = _('Rating')
        verbose_name_plural = _('Ratings')

    def __str__(self):
        return str(self.name)


class Content(BaseModel, SlugMixin):
    """Model definition for Content (Entity)."""
    STATUS_CHOICES = [
        ('P', _('Pending')),
        ('A', _('Airing')),
        ('F', _('Finished')),
        ('U', _('Upcoming'))
    ]
    CATEGORY_CHOICES = [
        ('P', _('Pending')),
        ('O', _('ONA')),
        ('S', _('Series')),
        ('M', _('Movies'))
    ]
    name = models.CharField(_('Name (ENG)'), max_length=255, unique=True)
    name_jpn = models.CharField(_('Name (JPN)'), max_length=255, unique=True)
    image = models.ImageField(_('Image'), upload_to='contents/')
    synopsis = models.TextField(_('Synopsis'))
    episodes = models.IntegerField(_('Episodes'), validators=[MinValueValidator(0), MaxValueValidator(1500)])
    duration = models.CharField(_('Duration'), max_length=20, help_text='Format: "25 min. per ep."')
    release = models.DateField(_('Release'))
    category = models.CharField(_('Category'), max_length=1, choices=CATEGORY_CHOICES, default='P')
    status = models.CharField(_('Status'), max_length=1, choices=STATUS_CHOICES, default='P')
    studio_id = models.ForeignKey(Studio, on_delete=models.CASCADE)
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE)
    season_id = models.ForeignKey(Season, on_delete=models.CASCADE)
    rating_id = models.ForeignKey(Rating, on_delete=models.CASCADE)
    url_id = models.ManyToManyField(Url)

    class Meta:
        """Meta definition for Content."""
        verbose_name = _('Content')
        verbose_name_plural = _('Contents')

    def __str__(self):
        return str(self.name)
