"""Admin for Animes App."""

from django.contrib import admin
from import_export import resources

from .models import Broadcast, Anime, AnimeStats


class AnimeResource(resources.ModelResource):

    class Meta:
        model = Anime


@admin.register(Broadcast)
class BroadcastAdmin(admin.ModelAdmin):
    """Admin for Broadcast model."""

    list_per_page = 25
    search_fields = ["string"]
    list_display = ["string", "is_available"]
    list_editable = ["is_available"]
    readonly_fields = ["pk", "created_at", "updated_at"]


@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    """Admin for Anime model."""

    list_per_page = 25
    # empty_value_display = "pending"
    search_fields = [
        "name",
        "name_jpn",
        "name_rom",
        "alternative_names",
    ]
    list_display = [
        "name",
        "is_available",
    ]
    list_filter = [
        "status",
        "genres",
        "studio_id",
    ]
    list_editable = [
        "is_available",
    ]
    readonly_fields = [
        "pk",
        "slug",
        "score",
        "ranked",
        "popularity",
        "favorites",
        "members",
        "created_at",
        "updated_at",
    ]
    autocomplete_fields = [
        "studio_id",
        "broadcast_id",
    ]
    filter_horizontal = [
        "producers",
        "genres",
        "themes",
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
        "is_available",
    ]
    list_filter = [
        "is_available",
    ]
    list_editable = [
        "is_available",
    ]
    readonly_fields = [
        "pk",
        "created_at",
        "updated_at",
    ]
