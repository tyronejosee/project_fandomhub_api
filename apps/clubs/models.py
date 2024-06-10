"""Models for Clubs App."""

from django.conf import settings
from django.db import models
from django.db.models import UniqueConstraint
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext as _

from apps.utils.models import BaseModel
from apps.utils.mixins import SlugMixin
from apps.utils.validators import FileSizeValidator, ImageSizeValidator
from apps.utils.paths import image_path
from .managers import ClubManager, ClubMemberManager
from .choices import CategoryChoices

User = settings.AUTH_USER_MODEL


class Club(BaseModel, SlugMixin):
    """Model definition for Club."""

    name = models.CharField(_("name"), max_length=255)
    description = models.TextField(_("description"))
    image = models.ImageField(
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
    category = models.CharField(
        _("category"),
        max_length=30,
        choices=CategoryChoices.choices,
    )
    members = models.PositiveIntegerField(_("members"), default=0)
    created_by = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        db_index=True,
        verbose_name=_("creator"),
    )
    is_public = models.BooleanField(_("is public"))

    objects = ClubManager()

    class Meta:
        ordering = ["pk"]
        verbose_name = _("club")
        verbose_name_plural = _("clubs")

    def __str__(self):
        return str(self.name)


class ClubMember(BaseModel):
    """Model definition for ClubMember."""

    club_id = models.ForeignKey(
        Club,
        on_delete=models.CASCADE,
        verbose_name=_("club"),
    )
    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_("user"),
    )
    joined_at = models.DateTimeField(_("joined_at"), auto_now_add=True)

    objects = ClubMemberManager()

    class Meta:
        ordering = ["-created_at"]
        verbose_name = _("club member")
        verbose_name_plural = _("club members")
        constraints = [
            UniqueConstraint(fields=["club_id", "user_id"], name="unique_club_user")
        ]

    def __str__(self):
        return str(self.user.username)


class Event(BaseModel):
    """Model definition for Event."""

    club_id = models.ForeignKey(
        Club,
        on_delete=models.CASCADE,
        limit_choices_to={"is_available": True},
        verbose_name=_("club"),
    )
    name = models.CharField(_("name"), max_length=255)
    description = models.TextField(_("description"))
    date = models.DateTimeField(_("date"))

    class Meta:
        ordering = ["-created_at"]
        verbose_name = _("event")
        verbose_name_plural = _("events")

    def __str__(self):
        return str(self.name)


class Topic(BaseModel):
    """Model definition for Topic."""

    name = models.CharField(_("name"), max_length=255)
    club_id = models.ForeignKey(
        Club,
        on_delete=models.CASCADE,
        limit_choices_to={"is_available": True},
        verbose_name=_("topic"),
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_("created by"),
    )

    class Meta:
        ordering = ["pk"]
        verbose_name = _("topic")
        verbose_name_plural = _("topics")

    def __str__(self):
        return str(self.name)


class Discussion(BaseModel):
    """Model definition for Discussion."""

    topic_id = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        limit_choices_to={"is_available": True},
        verbose_name=_("topic"),
    )
    content = models.TextField(_("content"))
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_("created by"),
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = _("discussion")
        verbose_name_plural = _("discussions")

    def __str__(self):
        return str(f"{self.created_by} - {self.content}")
