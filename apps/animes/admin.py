"""Admin for Animes App."""

from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from import_export.admin import ImportExportModelAdmin

from apps.utils.admin import BaseAdmin
from apps.utils.models import Picture
from .models import Broadcast, Anime, AnimeStats
from .resources import BroadcastResource, AnimeResource, AnimeStatsResource


class PictureInline(GenericTabularInline):
    model = Picture


@admin.register(Broadcast)
class BroadcastAdmin(ImportExportModelAdmin, BaseAdmin):
    """Admin for Broadcast model."""

    search_fields = ["string"]
    list_display = ["string", "is_available"]
    list_editable = ["is_available"]
    readonly_fields = ["pk", "created_at", "updated_at"]
    resource_class = BroadcastResource


@admin.register(Anime)
class AnimeAdmin(ImportExportModelAdmin, BaseAdmin):
    """Admin for Anime model."""

    search_fields = ["name", "name_jpn", "name_rom", "alternative_names"]
    list_display = ["name", "is_available"]
    list_filter = ["status", "genres", "studio_id"]
    list_editable = ["is_available"]
    readonly_fields = [
        "pk",
        "slug",
        "created_at",
        "updated_at",
    ]
    autocomplete_fields = ["studio_id", "broadcast_id"]
    filter_horizontal = ["producers", "genres", "themes"]
    inlines = [PictureInline]
    resource_class = AnimeResource


@admin.register(AnimeStats)
class AnimeStatsAdmin(ImportExportModelAdmin, BaseAdmin):
    """Admin for AnimeStats model."""

    search_fields = ["anime_id"]
    list_display = ["anime_id", "is_available"]
    list_filter = ["is_available"]
    list_editable = ["is_available"]
    readonly_fields = ["pk", "created_at", "updated_at"]
    resource_class = AnimeStatsResource
