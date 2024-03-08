"""Model Translation Configs."""

from modeltranslation.translator import TranslationOptions, register
from apps.contents.models import Anime


@register(Anime)
class AnimeTranslationOptions(TranslationOptions):
    """"Model translations config for Anime model."""
    fields = ("synopsis",)
