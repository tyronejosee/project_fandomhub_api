"""Choices for Characters App."""

from django.db.models import TextChoices

from django.utils.translation import gettext as _


class RoleChoices(TextChoices):

    MAIN = "main", _("Main")
    SUPPORTING = "supporting", _("Supporting")

    # TODO: Add more


class LanguageChoices(TextChoices):

    JAPANESE = "japanese", _("Japanese")
    ENGLISH = "english", _("English")
    SPANISH = "spanish", _("Spanish")
    FRENCH = "french", _("French")
    GERMAN = "german", _("German")
    ITALIAN = "italian", _("Italian")
    PORTUGUESE = "portuguese", _("Portuguese")
