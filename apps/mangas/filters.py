"""Filters for Mangas App."""

from django_filters import rest_framework as filters

from .models import Manga
from .choices import MediaTypeChoices, StatusChoices


class MangaMinimalFilter(filters.FilterSet):
    """Filter for Anime model (Minimal)."""

    media_type = filters.ChoiceFilter(choices=MediaTypeChoices.choices)
    status = filters.ChoiceFilter(choices=StatusChoices.choices)

    class Meta:
        model = Manga
        fields = [
            "media_type",
            "status",
        ]
