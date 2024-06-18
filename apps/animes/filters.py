"""Filters for Animes App."""

from django_filters import rest_framework as filters

from apps.utils.filters import BaseFilter
from .models import Anime
from .choices import MediaTypeChoices, StatusChoices, RatingChoices


class AnimeFilter(BaseFilter):
    """Filter for Anime model."""

    genre = filters.CharFilter(field_name="genres__name", lookup_expr="icontains")
    theme = filters.CharFilter(field_name="themes__name", lookup_expr="icontains")
    min_score = filters.NumberFilter(field_name="score", lookup_expr="gte")
    max_score = filters.NumberFilter(field_name="score", lookup_expr="lte")

    class Meta:
        model = Anime
        fields = ["sort", "letter"]


class AnimeMinimalFilter(filters.FilterSet):
    """Filter for Anime model (Minimal)."""

    media_type = filters.ChoiceFilter(choices=MediaTypeChoices.choices)
    status = filters.ChoiceFilter(choices=StatusChoices.choices)
    rating = filters.ChoiceFilter(choices=RatingChoices.choices)

    class Meta:
        model = Anime
        fields = [
            "media_type",
            "status",
            "rating",
        ]
