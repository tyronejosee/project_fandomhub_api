"""Models for Profiles App."""

from django.conf import settings
from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext as _

from apps.utils.models import BaseModel
from apps.utils.validators import FileSizeValidator, ImageSizeValidator
from apps.utils.paths import profile_image_path
from .managers import ProfileManager

User = settings.AUTH_USER_MODEL


class Profile(BaseModel):
    """Model definition for Profile."""

    user_id = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile",
        db_index=True,
        verbose_name=_("user"),
    )
    first_name = models.CharField(_("first name"), max_length=255, blank=True)
    last_name = models.CharField(_("last name"), max_length=255, blank=True)
    birth_date = models.DateField(_("birth date"), blank=True, null=True)
    bio = models.TextField(_("bio"), default="", blank=True)
    image = models.ImageField(
        _("image"),
        upload_to=profile_image_path,
        blank=True,
        null=True,
        validators=[
            FileExtensionValidator(allowed_extensions=["jpg", "png", "webp"]),
            ImageSizeValidator(max_width=600, max_height=600),
            FileSizeValidator(limit_mb=1),
        ],
    )
    cover = models.ImageField(
        _("cover"),
        upload_to=profile_image_path,
        blank=True,
        null=True,
        validators=[
            FileExtensionValidator(allowed_extensions=["jpg", "png", "webp"]),
            ImageSizeValidator(max_width=1200, max_height=600),
            FileSizeValidator(limit_mb=1),
        ],
    )

    objects = ProfileManager()

    class Meta:
        ordering = ["pk"]
        verbose_name = _("profile")
        verbose_name_plural = _("profiles")

    def __str__(self):
        return str(self.user_id.username)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
