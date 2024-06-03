"""Choices for Persons App."""

from django.db.models import TextChoices
from django.utils.translation import gettext as _


class LanguageChoices(TextChoices):

    JAPANESE = "japanese", _("Japanese")
    ENGLISH = "english", _("English")
    SPANISH = "spanish", _("Spanish")
    FRENCH = "french", _("French")
    GERMAN = "german", _("German")
    ITALIAN = "italian", _("Italian")
    PORTUGUESE = "portuguese", _("Portuguese")


class CategoryChoices(TextChoices):

    DIRECTOR = "director", _("Director")
    VOICE_ACTOR = "voice_actor", _("Voice Actor")
    ARTIST = "artist", _("Artist")
    WRITER = "writer", _("Writer")
    PRODUCER = "producer", _("Producer")
    OTHER = "other", _("Other")
