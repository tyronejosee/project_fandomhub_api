"""Models for Playlists App."""

from django.conf import settings
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext as _

from apps.utils.models import BaseModel
from apps.utils.validators import FileSizeValidator, ImageSizeValidator
from apps.utils.paths import image_path
from .managers import PlaylistManager
from .choices import StatusChoices

User = settings.AUTH_USER_MODEL


class Tag(BaseModel):
    """Model definition for Tag."""

    name = models.CharField(_("name"), max_length=100)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, db_index=True, verbose_name=_("user")
    )

    class Meta:
        ordering = ["pk"]
        verbose_name = _("tag")
        verbose_name_plural = _("tags")

    def __str__(self):
        return str(f"{self.user} - {self.name}")


class Playlist(BaseModel):
    """Model definition for Playlist."""

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, db_index=True, verbose_name=_("user")
    )
    name = models.CharField(_("name"), max_length=100, unique=True)
    description = models.TextField(_("description"), blank=True, null=True)
    tags = models.ManyToManyField("Tag", verbose_name=_("tags"), blank=True)
    number_items = models.IntegerField(_("number of items"), default=0)
    cover = models.ImageField(
        _("image"),
        upload_to=image_path,
        blank=True,
        null=True,
        validators=[
            FileExtensionValidator(allowed_extensions=["jpg", "png", "webp"]),
            ImageSizeValidator(max_width=600, max_height=600),
            FileSizeValidator(limit_mb=1),
        ],
    )
    is_public = models.BooleanField(_("is public"), default=True)

    objects = PlaylistManager()

    # TODO: Add number_item logic

    class Meta:
        ordering = ["pk"]
        verbose_name = _("playlist")
        verbose_name_plural = _("playlists")

    def __str__(self):
        return str(f"{self.user} - {self.name}")


class PlaylistItem(BaseModel):
    """Model definition for PlaylistItem."""

    playlist = models.ForeignKey(
        Playlist, on_delete=models.CASCADE, db_index=True, verbose_name=_("playlist")
    )
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.UUIDField()
    content_object = GenericForeignKey("content_type", "object_id")
    status = models.CharField(
        _("status"),
        max_length=20,
        choices=StatusChoices.choices,
        default=StatusChoices.PENDING,
        db_index=True,
    )
    is_watched = models.BooleanField(_("is watched"), default=False, db_index=True)
    is_favorite = models.BooleanField(_("is favorite"), default=False, db_index=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["pk"]
        verbose_name = _("playlist item")
        verbose_name_plural = _("playlist items")

    def __str__(self):
        return str(f"{self.playlist} - {self.object_id}")
