"""Filters for Reviews App."""

from django.db.models import TextChoices
from django.utils.translation import gettext as _
from django.contrib.contenttypes.models import ContentType
import django_filters as filters

from apps.animes.models import Anime
from apps.mangas.models import Manga
from .models import Review


class ReviewFilter(filters.FilterSet):
    """Filter for Anime model."""

    class TypeChoices(TextChoices):

        ANIME = "anime", _("Anime")
        MANGA = "manga", _("Manga")

    type = filters.ChoiceFilter(
        choices=TypeChoices.choices,
        method="filter_by_type",
        label=_("The type of reviews to filter by"),
    )
    spoilers = filters.BooleanFilter(
        field_name="is_spoiler",
        initial=True,
        method="filter_spoilers",
        label=_(
            "Whether the results include reviews with spoilers or not. Defaults to true"
        ),
    )

    class Meta:
        model = Review
        fields = [
            "type",
            "rating",
            "spoilers",
        ]

    def filter_by_type(self, queryset, name, value):
        if value == "anime":
            content_type = ContentType.objects.get_for_model(Anime)
        elif value == "manga":
            content_type = ContentType.objects.get_for_model(Manga)
        else:
            return queryset
        return queryset.filter(content_type=content_type)

    def filter_spoilers(self, queryset, name, value):
        if value:
            return queryset
        else:
            return queryset.filter(is_spoiler=False)


class ReviewMinimalFilter(filters.FilterSet):
    """Filter for Review model (Animes)."""

    spoilers = filters.BooleanFilter(
        field_name="is_spoiler",
        initial=True,
        method="filter_spoilers",
        label=_(
            "Whether the results include reviews with spoilers or not. Defaults to true"
        ),
    )
    # preliminary (boolean)

    class Meta:
        model = Review
        fields = [
            "spoilers",
        ]

    def filter_spoilers(self, queryset, name, value):
        if value:
            return queryset
        else:
            return queryset.filter(is_spoiler=False)
