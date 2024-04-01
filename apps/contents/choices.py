"""Choices for Contents App."""

from django.utils.translation import gettext as _


STATUS_CHOICES = [
    ("pending", _("Pending")),
    ("finished", _("Finished")),
    ("airing", _("Airing")),
    ("upcoming", _("Upcoming"))
]

CATEGORY_CHOICES = [
    ("pending", _("Pending")),
    ("tv", _("TV")),
    ("ova", _("OVA")),
    ("movie", _("Movie")),
    ("special", _("Special")),
    ("ona", _("ONA")),
    ("music", _("Music")),
]

RATING_CHOICES = [
    ("pending", _("Pending")),
    ("g", _("G - All Ages")),
    ("pg", _("PG - Children")),
    ("pg13", _("PG-13 - Teens 13 and Older")),
    ("r", _("R - 17+ (Violence & Profanity)")),
    ("rplus", _("R+ - Profanity & Mild Nudity")),
    ("rx", _("RX - Hentai")),
]

MEDIA_TYPE_CHOICES = [
    ("pending", _("Pending")),
    ("manga", _("Manga")),
    ("novel", _("Novel")),
    ("oneshot", _("One Shot")),
    ("doujinshi", _("Doujinshi")),
    ("manhwa", _("Manhwa")),
    ("oel", _("OEL")),
]

SOURCE_CHOICES = [
    ("pending", _("Pending")),
    ("original", _("Original")),
    ("manga", _("Manga")),
    ("novel", _("Novel")),
    ("lnovel", _("Light Novel")),
    ("vnovel", _("Visual Novel")),
    ("game", _("Game")),
    ("book", _("Book")),
    ("radio", _("Radio")),
    ("music", _("Music")),
]
