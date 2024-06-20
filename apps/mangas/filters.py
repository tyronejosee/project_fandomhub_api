"""Filters for Mangas App."""

from django.utils.translation import gettext as _
from django_filters import rest_framework as filters

from apps.utils.filters import BaseFilter
from .models import Magazine, Manga
from .choices import OrderByChoices, MediaTypeChoices, StatusChoices


class MagazineFilter(BaseFilter):
    """Filter for Magazine model."""

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


class MangaMinimalFilter(filters.FilterSet):
    """Filter for Anime model (Minimal)."""

    media_type = filters.ChoiceFilter(
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
            "media_type",
            "status",
        ]
