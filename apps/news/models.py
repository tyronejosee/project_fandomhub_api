"""Models for News App."""

from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _

from apps.utils.models import BaseModel
from .managers import NewManager
from .choices import TAG_CHOICES

User = settings.AUTH_USER_MODEL


class New(BaseModel):
    """Model definition for New."""

    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("user"))
    title = models.CharField(_("title"), max_length=100)
    description = models.CharField(_("description"), max_length=255)
    content = models.TextField(_("content"))
    image = models.ImageField(_("image"), upload_to="news/")
    source = models.URLField(_("source"), max_length=255)
    tag = models.CharField(
        _("tag"), max_length=15, choices=TAG_CHOICES, default="pending"
    )

    objects = NewManager()

    class Meta:
        ordering = ["pk"]
        verbose_name = _("new")
        verbose_name_plural = _("news")
        indexes = [
            models.Index(fields=["title"], name="title_idx"),
            models.Index(fields=["tag"], name="tag_idx"),
        ]

    def __str__(self):
        return str(self.title)
