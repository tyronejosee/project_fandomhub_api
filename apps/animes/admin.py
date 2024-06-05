"""Admin for Animes App."""

from django.contrib import admin
from import_export import resources

from .models import Anime, AnimeStats


class BookResource(resources.ModelResource):

    class Meta:
        model = Anime


@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    """Admin for Anime model."""

    list_per_page = 25
    search_fields = [
        "name",
        "name_jpn",
        "name_rom",
    ]
    list_display = [
        "name",
        "available",
    ]
    list_filter = [
        "status",
        "genres",
        "studio",
    ]
    list_editable = [
        "available",
    ]
    readonly_fields = [
        "pk",
        "slug",
        "mean",
        "rank",
        "popularity",
        "favorites",
        "num_list_users",
        "created_at",
        "updated_at",
    ]
    autocomplete_fields = [
        "studio",
        "genres",
        "themes",
        "season",
    ]


@admin.register(AnimeStats)
class AnimeStatsAdmin(admin.ModelAdmin):
    """Admin for AnimeStats model."""

    list_per_page = 25
    search_fields = [
        "anime_id",
    ]
    list_display = [
        "anime_id",
        "available",
    ]
    list_filter = [
        "available",
    ]
    list_editable = [
        "available",
    ]
    readonly_fields = [
        "pk",
        "created_at",
        "updated_at",
    ]
