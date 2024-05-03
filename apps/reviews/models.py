"""Models for Reviews App."""

from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext as _

from apps.utils.models import BaseModel
from apps.contents.models import Anime, Manga
from .managers import ReviewAnimeManager, ReviewMangaManager

User = settings.AUTH_USER_MODEL


class ReviewBase(BaseModel):
    """Model definition for Review."""
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        db_index=True, verbose_name=_("user"))
    rating = models.IntegerField(
        _("rating"), validators=[MinValueValidator(1), MaxValueValidator(10)])
    comment = models.TextField(_("comment"))

    class Meta:
        """Meta definition for ReviewBase."""
        abstract = True


class ReviewAnime(ReviewBase):
    """Model definition for ReviewAnime (Pivot)."""
    anime = models.ForeignKey(
        Anime, on_delete=models.CASCADE,
        related_name="review_anime", verbose_name=_("anime"))

    objects = ReviewAnimeManager()

    def __str__(self):
        return str(f"{self.user} {self.anime}")


class ReviewManga(ReviewBase):
    """Model definition for ReviewManga (Pivot)."""
    manga = models.ForeignKey(
        Manga, on_delete=models.CASCADE,
        related_name="review_manga", verbose_name=_("manga"))

    objects = ReviewMangaManager()

    def __str__(self):
        return str(f"{self.user} {self.manga}")
