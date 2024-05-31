"""Models for Genres App."""

from django.db import models
from django.utils.translation import gettext as _

from apps.utils.models import BaseModel
from apps.utils.mixins import SlugMixin
from .managers import GenreManager


class Genre(BaseModel, SlugMixin):
    """Model definition for Genre."""

    name = models.CharField(_("name"), max_length=255)

    objects = GenreManager()

    class Meta:
        ordering = ["pk"]
        verbose_name = _("genre")
        verbose_name_plural = _("genres")

    def __str__(self):
        return str(self.name)
