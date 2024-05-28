"""Models for Categories App."""

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext as _

from apps.utils.paths import image_path
from apps.utils.models import BaseModel
from apps.utils.validators import FileSizeValidator, ImageSizeValidator
from apps.utils.mixins import SlugMixin
from .managers import (
    StudioManager,
    GenreManager,
    ThemeManager,
    SeasonManager,
    DemographicManager,
)
from .choices import SeasonChoices


class Studio(BaseModel, SlugMixin):
    """Model definition for Studio."""

    name = models.CharField(_("name (eng)"), max_length=255, unique=True)
    name_jpn = models.CharField(_("name (jpn)"), max_length=255, unique=True)
    established = models.CharField(
        _("established"), max_length=255, blank=True, null=True
    )
    image = models.ImageField(
        _("image"),
        blank=True,
        null=True,
        upload_to=image_path,
        validators=[
            FileExtensionValidator(allowed_extensions=["webp"]),
            ImageSizeValidator(max_width=1080, max_height=1080),
            FileSizeValidator(limit_mb=1),
        ],
    )

    objects = StudioManager()

    class Meta:
        ordering = ["pk"]
        verbose_name = _("studio")
        verbose_name_plural = _("studios")

    def __str__(self):
        return str(self.name)


class Genre(BaseModel, SlugMixin):
    """Model definition for Genre."""

    name = models.CharField(_("name"), max_length=255, unique=True)

    objects = GenreManager()

    class Meta:
        ordering = ["pk"]
        verbose_name = _("genre")
        verbose_name_plural = _("genres")

    def __str__(self):
        return str(self.name)


class Theme(BaseModel, SlugMixin):
    """Model definition for Theme."""

    name = models.CharField(_("name"), max_length=255, unique=True)

    objects = ThemeManager()

    class Meta:
        ordering = ["pk"]
        verbose_name = _("theme")
        verbose_name_plural = _("themes")

    def __str__(self):
        return str(self.name)


class Season(BaseModel):
    """Model definition for Season."""

    season = models.CharField(
        _("season"),
        max_length=10,
        choices=SeasonChoices.choices,
        default=SeasonChoices.PENDING,
    )
    year = models.IntegerField(
        _("year"),
        default=2010,
        db_index=True,
        validators=[MinValueValidator(1900), MaxValueValidator(2100)],
    )
    fullname = models.CharField(_("fullname"), max_length=255, unique=True, blank=True)

    objects = SeasonManager()

    class Meta:
        ordering = ["pk"]
        verbose_name = _("season")
        verbose_name_plural = _("season")

    def __str__(self):
        return str(self.fullname)

    def save(self, *args, **kwargs):
        # Override the save method to update the fullname field
        fullname_caps = self.season.capitalize()
        self.fullname = f"{fullname_caps} {self.year}"
        if Season.objects.filter(fullname=self.fullname).exists():
            raise ValidationError("The fullname field must be unique.")
        super().save(*args, **kwargs)


class Demographic(BaseModel):
    """Model definition for Demographic."""

    name = models.CharField(_("name"), max_length=50, unique=True)

    objects = DemographicManager()

    class Meta:
        ordering = ["pk"]
        verbose_name = _("demographic")
        verbose_name_plural = _("demographics")

    def __str__(self):
        return str(self.name)
