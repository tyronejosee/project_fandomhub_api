"""Admin for Playlists App."""

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from apps.utils.admin import BaseAdmin
from .models import AnimeList, MangaList, AnimeListItem, MangaListItem
from .resources import (
    AnimeListResource,
    MangaListResource,
    AnimeListItemResource,
    MangaListItemResource,
)


@admin.register(AnimeList)
class AnimeListAdmin(ImportExportModelAdmin, BaseAdmin):
    """Admin for AnimeList model."""

    ordering = ["-created_at"]
    search_fields = ["user"]
    list_display = ["user", "is_public", "is_available"]
    list_filter = ["is_available", "is_public"]
    readonly_fields = ["pk", "created_at", "updated_at"]
    resource_class = AnimeListResource


@admin.register(MangaList)
class MangaListAdmin(ImportExportModelAdmin, BaseAdmin):
    """Admin for MangaList model."""

    ordering = ["-created_at"]
    search_fields = ["user"]
    list_display = ["user", "is_public", "is_available"]
    list_filter = ["is_available", "is_public"]
    readonly_fields = ["pk", "created_at", "updated_at"]
    resource_class = MangaListResource


@admin.register(AnimeListItem)
class AnimeListItemAdmin(ImportExportModelAdmin, BaseAdmin):
    """Admin for AnimeListItem model."""

    ordering = ["-created_at"]
    search_fields = ["anime_id"]
    list_display = ["animelist_id", "anime_id", "is_available"]
    list_filter = ["status", "is_watched"]
    readonly_fields = ["pk", "created_at", "updated_at"]
    resource_class = AnimeListItemResource


@admin.register(MangaListItem)
class MangaListItemItemAdmin(ImportExportModelAdmin, BaseAdmin):
    """Admin for MangaListItem model."""

    ordering = ["-created_at"]
    search_fields = ["manga_id"]
    list_display = ["mangalist_id", "manga_id", "is_available"]
    list_filter = ["status", "is_read"]
    readonly_fields = ["pk", "created_at", "updated_at"]
    resource_class = MangaListItemResource
