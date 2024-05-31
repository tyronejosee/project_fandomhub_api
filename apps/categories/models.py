"""Models for Categories App."""

from django.db import models
from django.utils.translation import gettext as _

from apps.utils.models import BaseModel
from apps.utils.mixins import SlugMixin
from .managers import ThemeManager, DemographicManager


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
