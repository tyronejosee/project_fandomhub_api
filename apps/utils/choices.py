"""Choices for Utils App."""

from django.db.models import TextChoices
from django.utils.translation import gettext as _


class SortChoices(TextChoices):

    ASC = "asc", _("Ascending")
    DESC = "desc", _("Descending")
