"""Models for Utils App."""

import uuid
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

from .validators import FileSizeValidator, ImageSizeValidator
from .functions import generate_random_code
from .paths import picture_image_path


class BaseModel(models.Model):
    """Model definition for BaseModel (Base)."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_available = models.BooleanField(_("is available"), default=True, db_index=True)
    created_at = models.DateField(_("created at"), auto_now=False, auto_now_add=True)
    updated_at = models.DateField(_("updated at"), auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True


class Picture(BaseModel):
    """Model definition for Picture."""

    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to={"model__in": ["anime", "manga", "character", "person"]},
    )
    object_id = models.UUIDField()
    content_object = GenericForeignKey("content_type", "object_id")
    name = models.CharField(_("name"), max_length=100, default=generate_random_code)
    image = models.ImageField(
        _("image"),
        blank=True,
        null=True,
        upload_to=picture_image_path,
        validators=[
            FileExtensionValidator(allowed_extensions=["jpg", "png", "webp"]),
            ImageSizeValidator(max_width=3000, max_height=3000),
            FileSizeValidator(limit_mb=1),
        ],
    )

    class Meta:
        ordering = ["pk"]
        verbose_name = _("picture")
        verbose_name_plural = _("pictures")
        indexes = [
            models.Index(fields=["content_type", "object_id"]),
        ]

    def __str__(self):
        return str(self.content_object)

    def save(self, *args, **kwargs):
        # Override the method to validate the limit of polymorphic tables
        if self.content_type.model not in ["anime", "manga", "character", "person"]:
            raise ValidationError(_("Invalid model relationship"))
        super(Picture, self).save(*args, **kwargs)


class Video(BaseModel):
    """Model definition for Video."""

    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to={"model__in": ["anime", "manga"]},
    )
    object_id = models.UUIDField()
    content_object = GenericForeignKey("content_type", "object_id")
    video = models.URLField(_("video"))

    class Meta:
        ordering = ["pk"]
        verbose_name = _("video")
        verbose_name_plural = _("videos")
        indexes = [
            models.Index(fields=["content_type", "object_id"]),
        ]

    def __str__(self):
        return str(self.content_object)

    def save(self, *args, **kwargs):
        # Override the method to validate the limit of polymorphic tables
        if self.content_type.model not in ["anime", "manga"]:
            raise ValidationError(_("Invalid model relationship"))
        super(Video, self).save(*args, **kwargs)
