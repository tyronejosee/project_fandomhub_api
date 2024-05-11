"""Models for Utils App."""

import uuid
from django.db import models
from django.utils.translation import gettext as _


class BaseModel(models.Model):
    """Model definition for BaseModel (Base)."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    available = models.BooleanField(
        _("available"), default=True, db_index=True)
    created_at = models.DateField(
        _("created at"), auto_now=False, auto_now_add=True)
    updated_at = models.DateField(
        _("updated at"), auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True
