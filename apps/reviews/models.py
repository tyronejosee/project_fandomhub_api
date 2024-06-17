"""Models for Reviews App."""

from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext as _

from apps.utils.models import BaseModel
from .managers import ReviewManager

User = settings.AUTH_USER_MODEL


class Review(BaseModel):
    """Model definition for Review."""

    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        db_index=True,
        verbose_name=_("user"),
    )
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.UUIDField()
    content_object = GenericForeignKey("content_type", "object_id")
    rating = models.IntegerField(
        _("rating"),
        validators=[MinValueValidator(1), MaxValueValidator(10)],
    )
    comment = models.TextField(_("comment"))
    is_spoiler = models.BooleanField(_("is spoiler"), default=False)
    helpful_count = models.PositiveIntegerField(_("helpful count"), default=0)
    reported_count = models.PositiveIntegerField(_("reported count"), default=0)

    objects = ReviewManager()

    class Meta:
        ordering = ["-created_at"]
        verbose_name = _("review")
        verbose_name_plural = _("reviews")
        indexes = [
            models.Index(fields=["content_type", "object_id"]),
        ]
        constraints = [
            models.UniqueConstraint(
                fields=["content_type", "object_id", "user_id"],
                name="unique_content_user",
            )
        ]

    def __str__(self):
        return str(f"{self.user_id} - {self.content_object}")
