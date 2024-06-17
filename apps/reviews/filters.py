"""Filters for Reviews App."""

from django.contrib.contenttypes.models import ContentType
import django_filters as filters

from apps.animes.models import Anime
from apps.mangas.models import Manga
from .models import Review


class ReviewFilter(filters.FilterSet):
    """Filter for Anime model."""

    type = filters.ChoiceFilter(
        choices=[
            ("anime", "Anime"),
            ("manga", "Manga"),
        ],
        method="filter_by_type",
    )

    class Meta:
        model = Review
        fields = [
            "type",
            "rating",
            "is_spoiler",
        ]

    def filter_by_type(self, queryset, name, value):
        if value == "anime":
            content_type = ContentType.objects.get_for_model(Anime)
        elif value == "manga":
            content_type = ContentType.objects.get_for_model(Manga)
        else:
            return queryset

        return queryset.filter(content_type=content_type)
