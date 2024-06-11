"""Admin for Animes App."""

from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from import_export import resources

from apps.utils.admin import BaseAdmin
from apps.utils.models import Picture
from .models import Broadcast, Anime, AnimeStats


class AnimeResource(resources.ModelResource):

    class Meta:
        model = Anime


class PictureInline(GenericTabularInline):
    model = Picture


@admin.register(Broadcast)
class BroadcastAdmin(BaseAdmin):
    """Admin for Broadcast model."""

    search_fields = ["string"]
    list_display = ["string", "is_available"]
    list_editable = ["is_available"]
    readonly_fields = ["pk", "created_at", "updated_at"]


@admin.register(Anime)
class AnimeAdmin(BaseAdmin):
    """Admin for Anime model."""

    search_fields = ["name", "name_jpn", "name_rom", "alternative_names"]
    list_display = ["name", "is_available"]
    list_filter = ["status", "genres", "studio_id"]
    list_editable = ["is_available"]
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
    autocomplete_fields = ["studio_id", "broadcast_id"]
    filter_horizontal = ["producers", "genres", "themes"]
    inlines = [PictureInline]


@admin.register(AnimeStats)
class AnimeStatsAdmin(BaseAdmin):
    """Admin for AnimeStats model."""

    search_fields = ["anime_id"]
    list_display = ["anime_id", "is_available"]
    list_filter = ["is_available"]
    list_editable = ["is_available"]
    readonly_fields = ["pk", "created_at", "updated_at"]
