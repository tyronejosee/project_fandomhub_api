"""Choices for Persons App."""

from django.db.models import TextChoices
from django.utils.translation import gettext as _


class CategoryChoices(TextChoices):

    DIRECTOR = "director", _("Director")
    VOICE_ACTOR = "voice_actor", _("Voice Actor")
    ARTIST = "artist", _("Artist")
    WRITER = "writer", _("Writer")
    PRODUCER = "producer", _("Producer")
    OTHER = "other", _("Other")
