"""Admin for Playlists App."""

from django.contrib import admin

from apps.utils.admin import BaseAdmin
from .models import AnimeList, AnimeListItem, MangaList, MangaListItem


@admin.register(AnimeList)
class AnimeListAdmin(BaseAdmin):
    """Admin for AnimeList model."""

    ordering = ["-created_at"]
    search_fields = ["user"]
    list_display = ["user", "is_public", "is_available"]
    list_filter = ["is_available", "is_public"]
    readonly_fields = ["pk", "created_at", "updated_at"]


@admin.register(AnimeListItem)
class AnimeListItemAdmin(BaseAdmin):
    """Admin for AnimeListItem model."""

    ordering = ["-created_at"]
    search_fields = ["anime_id"]
    list_display = ["animelist_id", "anime_id", "is_available"]
    list_filter = ["status", "is_watched"]
    readonly_fields = ["pk", "created_at", "updated_at"]


@admin.register(MangaList)
class MangaListAdmin(BaseAdmin):
    """Admin for MangaList model."""

    ordering = ["-created_at"]
    search_fields = ["user"]
    list_display = ["user", "is_public", "is_available"]
    list_filter = ["is_available", "is_public"]
    readonly_fields = ["pk", "created_at", "updated_at"]


@admin.register(MangaListItem)
class MangaListItemItemAdmin(BaseAdmin):
    """Admin for MangaListItem model."""

    ordering = ["-created_at"]
    search_fields = ["manga_id"]
    list_display = ["mangalist_id", "manga_id", "is_available"]
    list_filter = ["status", "is_read"]
    readonly_fields = ["pk", "created_at", "updated_at"]
