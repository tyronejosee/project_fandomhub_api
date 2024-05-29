"""Models for Characters App."""

from django.db import models

from apps.utils.models import BaseModel
from apps.utils.mixins import SlugMixin
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext as _

from apps.utils.validators import FileSizeValidator, ImageSizeValidator
from apps.utils.paths import image_path


class Character(BaseModel, SlugMixin):
    """Model definition for Character."""

    name = models.CharField(_("name"), max_length=255)
    name_kanji = models.CharField(_("name kanji"), max_length=255)
    favorites = models.PositiveIntegerField(_("favorites"), default=0)
    about = models.TextField(_("about"))
    image = models.ImageField(
        _("image"),
        upload_to=image_path,
        blank=True,
        null=True,
        validators=[
            FileExtensionValidator(allowed_extensions=["webp"]),
            ImageSizeValidator(max_width=600, max_height=600),
            FileSizeValidator(limit_mb=1),
        ],
    )
    # TODO: Add GenericForeignKey for Animes and Mangas

    class Meta:
        ordering = ["pk"]
        verbose_name = _("character")
        verbose_name_plural = _("characters")

    def __str__(self):
        return str(self.name)
