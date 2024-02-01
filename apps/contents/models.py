"""Models for Contents App."""

from django.db import models
from django.core.validators import MinValueValidator
from django.utils.translation import gettext as _
from apps.utils.models import BaseModel

# TODO: Add slugs fields

class Url(BaseModel):
    """Model definition for Url (Association)."""
    tag = models.CharField(max_length=100, unique=True)
    url = models.URLField()
    # SVGs, Imgs

    class Meta:
        """Meta definition for Url."""
        verbose_name = _('Url')
        verbose_name_plural = _('Urls')


class Studio(BaseModel):
    """Model definition for Studio (Catalog)."""
    name_eng = models.CharField(max_length=255, unique=True, help_text=_('Example: MAPPA'))
    name_jpn = models.CharField(max_length=255, unique=True)
    image = models.ImageField(_('Image'), upload_to='studios/')
    established = models.DateField()

    class Meta:
        """Meta definition for Studio."""
        verbose_name = _('Studio')
        verbose_name_plural = _('Studios')


class Genre(BaseModel):
    """Model definition for Genre (Catalog)."""
    name = models.CharField(max_length=255, unique=True, help_text=_('Example: Comedy'))

    class Meta:
        """Meta definition for Genre."""
        verbose_name = _('Genre')
        verbose_name_plural = _('Genres')


class Premiered(BaseModel):
    """Model definition for Premiered (Catalog)."""
    name = models.CharField(max_length=25, unique=True, help_text=_('Example: Winter 2024'))

    class Meta:
        """Meta definition for Premiered."""
        verbose_name = _('Premiered')
        verbose_name_plural = _('Premiered')


class Rating(BaseModel):
    """Model definition for Rating (Catalog)."""
    name = models.CharField(
        max_length=50, unique=True, help_text=_('Example: PG-13 - Teens 13 or older')
    )

    class Meta:
        """Meta definition for Rating."""
        verbose_name = _('Rating')
        verbose_name_plural = _('Ratings')

    def __str__(self):
        return str(self.name)


class Content(BaseModel):
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
    title_eng = models.CharField(_('Title - English'), max_length=255, unique=True)
    title_jpn = models.CharField(_('Title - Japanese'), max_length=255, unique=True)
    image = models.ImageField(_('Image'), upload_to='contents/')
    synopsis = models.TextField(_('Synopsis'))
    episodes = models.IntegerField(_('Episodes'), validators=[MinValueValidator(0)])
    duration = models.CharField(_('Duration'), max_length=20, help_text='Format: "25 min. per ep."')
    release = models.DateField(_('Release'))
    category = models.CharField(_('Category'), max_length=1, choices=CATEGORY_CHOICES, default='P')
    status = models.CharField(_('Status'), max_length=1, choices=STATUS_CHOICES, default='P')
    studio_id = models.ForeignKey(Studio, on_delete=models.CASCADE)
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE)
    premiered_id = models.ForeignKey(Premiered, on_delete=models.CASCADE)
    rating_id = models.ForeignKey(Rating, on_delete=models.CASCADE)
    url_id = models.ForeignKey(Url, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Content."""
        verbose_name = _('Content')
        verbose_name_plural = _('Contents')

    def __str__(self):
        return f'{self.title_eng}'
