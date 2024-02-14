"""Models for Categories App."""

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext as _
from apps.utils.paths import image_path
from apps.utils.models import BaseModel
from apps.utils.mixins import SlugMixin
from apps.categories.choices import TAG_CHOICES, SEASON_CHOICES


class Url(BaseModel):
    """Model definition for Url (Association)."""
    url = models.URLField(_('URL'))
    tag = models.IntegerField(_('Tag'), choices=TAG_CHOICES, default=0)

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


class Season(BaseModel):
    """Model definition for Season (Catalog)."""
    season = models.IntegerField(_('Season'), choices=SEASON_CHOICES, default=0)
    year = models.IntegerField(
        _('Year'), validators=[MinValueValidator(1900), MaxValueValidator(2100)], default=2010
    )

    class Meta:
        """Meta definition for Season."""
        verbose_name = _('Season')
        verbose_name_plural = _('Season')

    def get_season_display_name(self):
        """Gets the season name based on the season value."""
        for choice in SEASON_CHOICES:
            if choice[0] == self.season:
                return choice[1]
        return _('Pending')

    def __str__(self):
        return f'{self.get_season_display_name()} {self.year}'


class Demographic(BaseModel):
    """Model definition for Demographic (Catalog)."""
    name = models.CharField(_('Name'), max_length=50, unique=True)

    class Meta:
        """Meta definition for Demographic."""
        verbose_name = _('Demographic')
        verbose_name_plural = _('Demographics')

    def __str__(self):
        return str(self.name)
