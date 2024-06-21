"""Filters for Animes App."""

from django.utils.translation import gettext as _
from django_filters import rest_framework as filters

from apps.utils.filters import BaseFilter
from .models import Anime
from .choices import MediaTypeChoices, StatusChoices, RatingChoices


class AnimeFilter(BaseFilter):
    """Filter for Anime model."""

    min_score = filters.NumberFilter(
        field_name="score",
        lookup_expr="gte",
        label=_("Set a minimum score for results"),
    )
    max_score = filters.NumberFilter(
        field_name="score",
        lookup_expr="lte",
        label=_("Set a maximum score for results"),
    )
    rating = filters.ChoiceFilter(
        choices=RatingChoices.choices,
        label=_("Available Anime audience ratings"),
    )
    status = filters.ChoiceFilter(
        choices=StatusChoices.choices,
        label=_("Available Anime status"),
    )
    genre = filters.CharFilter(
        field_name="genres__name",
        lookup_expr="icontains",
        label=_("Filter by genre(s), e.g /?genre=gore"),
    )
    theme = filters.CharFilter(
        field_name="themes__name",
        lookup_expr="icontains",
        label=_("Filter by theme(s), e.g /?theme=shounen"),
    )
    start_date = filters.DateFilter(
        field_name="aired_from",
        lookup_expr="gte",
        label=_("Filter by starting date, Format: YYYY-MM-DD. e.g 2005-01-01"),
    )
    end_date = filters.DateFilter(
        field_name="aired_from",
        lookup_expr="lte",
        label=_("Filter by ending date, Format: YYYY-MM-DD. e.g 2005-01-01"),
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


class AnimeSeasonFilter(filters.FilterSet):
    """Filter for Anime model (Season)."""

    type = filters.ChoiceFilter(
        choices=MediaTypeChoices.choices,
        label=_("Available Anime types"),
    )

    # sfw (boolean)
    # unapproved (boolean)

    class Meta:
        model = Anime
        fields = [
            "type",
        ]
