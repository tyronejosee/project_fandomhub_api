"""Models for Persons App."""

from django.db import models
from django.utils.translation import gettext as _

from apps.utils.models import BaseModel


class Author(BaseModel):
    """Model definition for Author (Catalog)."""
    name = models.CharField(
        _("name"), max_length=255, unique=True, db_index=True
    )

    class Meta:
        """Meta definition for Author."""
        verbose_name = _("author")
        verbose_name_plural = _("authors")

    def __str__(self):
        return str(self.name)
