"""Models for Categories App."""

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext as _

from apps.utils.paths import image_path
from apps.utils.models import BaseModel
from apps.utils.mixins import SlugMixin
from .choices import SEASON_CHOICES


class Studio(BaseModel, SlugMixin):
    """Model definition for Studio (Catalog)."""
    name = models.CharField(
        _("name (eng)"), max_length=255, unique=True, db_index=True
    )
    name_jpn = models.CharField(_("name (jpn)"), max_length=255, unique=True)
    established = models.CharField(
        _("established"), max_length=255, blank=True, null=True
    )
    image = models.ImageField(
        _("image"), upload_to=image_path, blank=True, null=True
    )

    class Meta:
        """Meta definition for Studio."""
        verbose_name = _("studio")
        verbose_name_plural = _("studios")

    def __str__(self):
        return str(self.name)

    def get_image(self):
        """Returns the image URL or an empty string."""
        if self.image:
            return self.image.url
        return ""


class Genre(BaseModel, SlugMixin):
    """Model definition for Genre (Catalog)."""
    name = models.CharField(
        _("name"), max_length=255, unique=True, db_index=True
    )

    class Meta:
        """Meta definition for Genre."""
        verbose_name = _("genre")
        verbose_name_plural = _("genres")

    def __str__(self):
        return str(self.name)


class Theme(BaseModel, SlugMixin):
    """Model definition for Theme (Catalog)."""
    name = models.CharField(
        _("name"), max_length=255, unique=True, db_index=True
    )

    class Meta:
        """Meta definition for Theme."""
        verbose_name = _("theme")
        verbose_name_plural = _("themes")

    def __str__(self):
        return str(self.name)


class Season(BaseModel):
    """Model definition for Season (Catalog)."""
    season = models.IntegerField(
        _("season"), choices=SEASON_CHOICES, default=0
    )
    year = models.IntegerField(
        _("year"), default=2010, db_index=True,
        validators=[MinValueValidator(1900), MaxValueValidator(2100)]
    )
    fullname = models.CharField(_("fullname"), max_length=255, blank=True)

    class Meta:
        """Meta definition for Season."""
        verbose_name = _("season")
        verbose_name_plural = _("season")

    def __str__(self):
        return str(self.fullname)

    def get_season_display_name(self):
        """Gets the season name based on the season value."""
        for choice in SEASON_CHOICES:
            if choice[0] == self.season:
                return choice[1]
        return _("Pending")

    def save(self, *args, **kwargs):
        """Override the save method to update the fullname field."""
        self.fullname = f"{self.get_season_display_name()} {self.year}"
        super().save(*args, **kwargs)


class Demographic(BaseModel):
    """Model definition for Demographic (Catalog)."""
    name = models.CharField(
        _("name"), max_length=50, unique=True, db_index=True
    )

    class Meta:
        """Meta definition for Demographic."""
        verbose_name = _("demographic")
        verbose_name_plural = _("demographics")

    def __str__(self):
        return str(self.name)
