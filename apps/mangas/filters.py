"""Filters for Mangas App."""

from django.db.models import TextChoices
from django.utils.translation import gettext as _
from django_filters import rest_framework as filters

from apps.utils.filters import BaseFilter
from .models import Magazine, Manga
from .choices import MediaTypeChoices, StatusChoices


class MagazineFilter(BaseFilter):
    """Filter for Magazine model."""

    class OrderByChoices(TextChoices):

        ID = "id", _("UUID")
        NAME = "name", _("Name")
        COUNT = "count", _("Count")

    order_by = filters.ChoiceFilter(
        choices=OrderByChoices.choices,
        method="filter_order_by",
        label=_("Available Magazine order_by properties"),
    )

    def filter_order_by(self, queryset, name, value):
        return queryset.order_by(value)

    class Meta:
        model = Magazine
        fields = [
            "order_by",
            "sort",
            "letter",
        ]


class MangaFilter(BaseFilter):
    """Filter for Manga model."""

    min_score = filters.NumberFilter(
        field_name="score",
        lookup_expr="gte",
        label=_(
            "Set a minimum score for results, ex `/?min_score=5` or `/?min_score=5.5`"
        ),
    )
    max_score = filters.NumberFilter(
        field_name="score",
        lookup_expr="lte",
        label=_(
            "Set a maximum score for results, ex `/?max_score=7` or `/?max_score=7.8`"
        ),
    )
    type = filters.ChoiceFilter(
        field_name="media_type",
        choices=MediaTypeChoices.choices,
        label="Available Manga types, , ex `/?type=manga`",
    )
    status = filters.ChoiceFilter(
        choices=StatusChoices.choices,
        label=_("Available Manga status, ex `/?status=finished`"),
    )
    genre = filters.CharFilter(
        field_name="genres__name",
        lookup_expr="icontains",
        label=_("Filter by genre(s), ex `/?genre=gore`"),
    )
    theme = filters.CharFilter(
        field_name="themes__name",
        lookup_expr="icontains",
        label=_("Filter by theme(s), ex `/?theme=shounen`"),
    )
    start_date = filters.DateFilter(
        field_name="published_from",
        lookup_expr="gte",
        label=_("Filter by starting date, Format: `YYYY-MM-DD`. ex `2005-01-01`"),
    )
    end_date = filters.DateFilter(
        field_name="published_from",
        lookup_expr="lte",
        label=_("Filter by ending date, Format: `YYYY-MM-DD`. ex `2005-01-01`"),
    )

    class Meta:
        model = Manga
        fields = [
            "min_score",
            "max_score",
            "type",
            "status",
            "genre",
            "theme",
            "start_date",
            "end_date",
            "sort",
            "letter",
        ]


class MangaMinimalFilter(filters.FilterSet):
    """Filter for Anime model (Minimal)."""

    type = filters.ChoiceFilter(
        choices=MediaTypeChoices.choices,
        label=_("Available sorting properties by manga type"),
    )
    status = filters.ChoiceFilter(
        choices=StatusChoices.choices,
        label=_("Available sorting properties by manga status"),
    )

    class Meta:
        model = Manga
        fields = [
            "type",
            "status",
        ]
