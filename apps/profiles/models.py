"""Models for Profiles App."""

from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _

from apps.utils.models import BaseModel
from apps.utils.paths import profile_image_path

User = settings.AUTH_USER_MODEL


class Profile(BaseModel):
    """Model definition for Profile (Entity)."""
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name=_("user")
    )
    bio = models.TextField(_("bio"), blank=True, null=True)
    website = models.URLField(_("website"), blank=True, null=True)
    birth_date = models.DateField(_("birth date"), blank=True, null=True)
    image = models.ImageField(
        _("image"), upload_to=profile_image_path, blank=True, null=True
    )
    cover = models.ImageField(
        _("cover"), upload_to=profile_image_path, blank=True, null=True
    )

    class Meta:
        """Meta definition for Profile."""
        verbose_name = _("profile")
        verbose_name_plural = _("profiles")

    def __str__(self):
        return str(self.user.username)
