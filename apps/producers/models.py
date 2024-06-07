"""Models for Producers App."""

from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext as _

from apps.utils.paths import image_path
from apps.utils.models import BaseModel
from apps.utils.validators import FileSizeValidator, ImageSizeValidator
from apps.utils.mixins import SlugMixin
from .managers import ProducerManager
from .choices import TypeChoices


class Producer(BaseModel, SlugMixin):
    """Model definition for Producer."""

    name = models.CharField(_("name (eng)"), max_length=255, unique=True)
    name_jpn = models.CharField(_("name (jpn)"), max_length=255, unique=True)
    about = models.TextField(_("about"), blank=True)
    established = models.CharField(
        _("established"), max_length=255, blank=True, null=True
    )
    type = models.CharField(_("type"), max_length=15, choices=TypeChoices.choices)
    image = models.ImageField(
        _("image"),
        blank=True,
        null=True,
        upload_to=image_path,
        validators=[
            FileExtensionValidator(allowed_extensions=["jpg", "webp"]),
            ImageSizeValidator(max_width=600, max_height=600),
            FileSizeValidator(limit_mb=1),
        ],
    )
    favorites = models.PositiveIntegerField(_("favorites"), default=0)

    objects = ProducerManager()

    class Meta:
        ordering = ["pk"]
        verbose_name = _("producer")
        verbose_name_plural = _("producers")

    def __str__(self):
        return str(self.name)
