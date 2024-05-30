"""Models for Characters App."""

from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext as _

from apps.utils.models import BaseModel
from apps.utils.mixins import SlugMixin
from apps.utils.validators import FileSizeValidator, ImageSizeValidator
from apps.utils.paths import image_path
from apps.persons.models import Person
from .choices import RoleChoices, LanguageChoices


class Character(BaseModel, SlugMixin):
    """Model definition for Character."""

    name = models.CharField(_("name"), max_length=255)
    name_kanji = models.CharField(_("name kanji"), max_length=255)
    favorites = models.PositiveIntegerField(_("favorites"), default=0)
    about = models.TextField(_("about"), blank=True)
    role = models.CharField(_("role"), max_length=15, choices=RoleChoices.choices)
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
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.UUIDField()
    content_object = GenericForeignKey("content_type", "object_id")

    class Meta:
        ordering = ["pk"]
        verbose_name = _("character")
        verbose_name_plural = _("characters")

    def __str__(self):
        return str(self.name)


class CharacterVoice(BaseModel):
    """Model definition for CharacterVoice."""

    voice = models.ForeignKey(
        Person,
        on_delete=models.PROTECT,
        verbose_name=_("voice"),
    )
    character = models.ForeignKey(
        Character,
        on_delete=models.CASCADE,
        verbose_name=_("character"),
    )
    language = models.CharField(
        _("language"),
        max_length=20,
        choices=LanguageChoices.choices,
    )

    class Meta:
        ordering = ["pk"]
        verbose_name = _("character voice")
        verbose_name_plural = _("character voices")

    def __str__(self):
        return str(f"{self.character} - {self.voice}")
