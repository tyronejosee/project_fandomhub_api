"""Choices for Characters App."""

from django.db.models import TextChoices
from django.utils.translation import gettext as _


class RoleChoices(TextChoices):

    MAIN = "main", _("Main")
    SUPPORTING = "supporting", _("Supporting")
