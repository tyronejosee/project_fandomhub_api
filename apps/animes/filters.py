"""Filters for Animes App."""

from django_filters import rest_framework as filters

from apps.utils.filters import BaseFilter
from .models import Anime
from .choices import MediaTypeChoices, StatusChoices, RatingChoices


class AnimeFilter(BaseFilter):
    """Filter for Anime model."""

    min_score = filters.NumberFilter(
        field_name="score",
        lookup_expr="gte",
        label="Set a minimum score for results",
    )
    max_score = filters.NumberFilter(
        field_name="score",
        lookup_expr="lte",
        label="Set a maximum score for results",
    )
    rating = filters.ChoiceFilter(
        choices=RatingChoices.choices,
        label="Available Anime audience ratings",
    )
    status = filters.ChoiceFilter(
        choices=StatusChoices.choices,
        label="Available Anime status",
    )
    genre = filters.CharFilter(
        field_name="genres__name",
        lookup_expr="icontains",
    )
    theme = filters.CharFilter(
        field_name="themes__name",
        lookup_expr="icontains",
    )
    start_date = filters.DateFilter(
        field_name="aired_from",
        label="Filter by starting date",
        lookup_expr="gte",
        help_text="Format: YYYY-MM-DD. e.g 2005-01-01",
    )
    end_date = filters.DateFilter(
        field_name="aired_from",
        label="Filter by ending date",
        lookup_expr="lte",
        help_text="Format: YYYY-MM-DD. e.g 2005-01-01",
    )

    class Meta:
        model = Anime
        fields = [
            "min_score",
            "max_score",
            "rating",
            "status",
            "genre",
            "theme",
            "start_date",
            "end_date",
            "sort",
            "letter",
        ]


class AnimeMinimalFilter(filters.FilterSet):
    """Filter for Anime model (Minimal)."""

    type = filters.ChoiceFilter(
        choices=MediaTypeChoices.choices,
        label="Available Anime types",
    )
    status = filters.ChoiceFilter(
        choices=StatusChoices.choices,
        label="Available Anime status",
    )
    rating = filters.ChoiceFilter(
        choices=RatingChoices.choices,
        label="Available Anime audience ratings",
    )

    class Meta:
        model = Anime
        fields = [
            "type",
            "status",
            "rating",
        ]
