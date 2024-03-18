"""Models for Reviews App."""

from django.db import models
from django.conf import settings
from django.utils.translation import gettext as _
from apps.utils.models import BaseModel
from apps.contents.models import Anime

User = settings.AUTH_USER_MODEL


class Review(BaseModel):
    """Model definition for Review."""
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name=_("User")
    )
    anime = models.ForeignKey(
        Anime, on_delete=models.CASCADE, verbose_name=_("Anime")
    )
    rating = models.DecimalField(_("Rating"), max_digits=2, decimal_places=1)
    comment = models.TextField(_("Comment"))

    class Meta:
        """Meta definition for Review."""
        verbose_name = _("Review")
        verbose_name_plural = _("Reviews")

    def __str__(self):
        return str(self.comment)
