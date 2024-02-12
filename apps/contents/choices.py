"""Choices for Contents App."""

from django.utils.translation import gettext as _


STATUS_CHOICES = [
    (0, _('Pending')),
    (1, _('Finished')),
    (2, _('Airing')),
    (3, _('Upcoming'))
]

CATEGORY_CHOICES = [
    (0, _('Pending')),
    (1, _('TV')),
    (2, _('OVA')),
    (3, _('Movie')),
    (4, _('Special')),
    (5, _('ONA')),
    (6, _('Music')),
]

RATING_CHOICES = [
    (0, _('Pending')),
    (1, _('G - All Ages')),
    (2, _('PG - Children')),
    (3, _('PG-13 - Teens 13 and Older')),
    (4, _('R - 17+ (Violence & Profanity)')),
    (5, _('R+ - Profanity & Mild Nudity')),
    (6, _('RX - Hentai')),
]

MEDIA_TYPE_CHOICES = [
    ('0', _('Pending')),
    ('1', _('Manga')),
    ('2', _('Novel')),
    ('3', _('One Shot')),
    ('4', _('Doujinshi')),
    ('5', _('Manhwa')),
    ('6', _('OEL')),
]

SOURCE_CHOICES = [
    ('0', _('Pending')),
    ('1', _('Original')),
    ('2', _('Manga')),
    ('3', _('Novel')),
    ('4', _('Light Novel')),
    ('5', _('Visual Novel')),
    ('6', _('Game')),
    ('7', _('Book')),
    ('8', _('Radio')),
    ('9', _('Music')),
]
