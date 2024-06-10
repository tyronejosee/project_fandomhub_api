"""Admin for Playlists App."""

from django.contrib import admin

from .models import AnimeList, AnimeListItem, MangaList, MangaListItem


@admin.register(AnimeList)
class AnimeListAdmin(admin.ModelAdmin):
    """Admin for AnimeList model."""

    search_fields = ["user"]
    list_per_page = 25
    list_display = ["user", "is_public", "is_available"]
    list_filter = ["is_available", "is_public"]
    readonly_fields = ["pk", "created_at", "updated_at"]
    ordering = ["-created_at"]


@admin.register(AnimeListItem)
class AnimeListItemAdmin(admin.ModelAdmin):
    """Admin for AnimeListItem model."""

    search_fields = ["anime_id"]
    list_per_page = 25
    list_display = ["animelist_id", "anime_id", "is_available"]
    list_filter = ["status", "is_watched"]
    readonly_fields = ["pk", "created_at", "updated_at"]
    ordering = ["-created_at"]


@admin.register(MangaList)
class MangaListAdmin(admin.ModelAdmin):
    """Admin for MangaList model."""

    search_fields = ["user"]
    list_per_page = 25
    list_display = ["user", "is_public", "is_available"]
    list_filter = ["is_available", "is_public"]
    readonly_fields = ["pk", "created_at", "updated_at"]
    ordering = ["-created_at"]


@admin.register(MangaListItem)
class MangaListItemItemAdmin(admin.ModelAdmin):
    """Admin for MangaListItem model."""

    search_fields = ["manga_id"]
    list_per_page = 25
    list_display = ["mangalist_id", "manga_id", "is_available"]
    list_filter = ["status", "is_read"]
    readonly_fields = ["pk", "created_at", "updated_at"]
    ordering = ["-created_at"]
