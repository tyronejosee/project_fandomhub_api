"""Models for Categories App."""

from django.db import models
from django.utils.translation import gettext as _
from apps.utils.paths import image_path
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
    image = models.ImageField(_('Image'), upload_to=image_path, blank=True, null=True)

    class Meta:
        """Meta definition for Studio."""
        verbose_name = _('Studio')
        verbose_name_plural = _('Studios')

    def __str__(self):
        return str(self.name)

    def get_image(self):
        """Returns the image URL or an empty string."""
        if self.image:
            return str(self.image.url)
        return ''


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


class Demographic(BaseModel):
    """Model definition for Demographic (Catalog)."""
    name = models.CharField(_('Name'), max_length=50, unique=True)

    class Meta:
        """Meta definition for Demographic."""
        verbose_name = _('Demographic')
        verbose_name_plural = _('Demographics')

    def __str__(self):
        return str(self.name)


class Author(BaseModel):
    """Model definition for Author (Catalog)."""
    name = models.CharField(_('Name'), max_length=255, unique=True)

    class Meta:
        """Meta definition for Author."""
        verbose_name = _('Author')
        verbose_name_plural = _('Authors')

    def __str__(self):
        return str(self.name)
