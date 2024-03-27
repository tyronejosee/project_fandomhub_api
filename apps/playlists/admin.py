"""Admin for Playlists App."""

from django.contrib import admin

from .models import Playlist, PlaylistAnime, PlaylistManga


@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    """Admin config for Playlist model."""
    search_fields = ["user",]
    list_display = ["user",]
    list_per_page = 25
    readonly_fields = ["pk",]
    ordering = ["pk",]


@admin.register(PlaylistAnime)
class PlaylistAnimeAdmin(admin.ModelAdmin):
    """Admin config for PlaylistAnime model."""
    search_fields = ["playlist",]
    list_display = ["playlist",]
    list_filter = ["is_watched", "status"]
    list_per_page = 25
    readonly_fields = ["pk",]
    autocomplete_fields = ["anime"]
    ordering = ["pk",]    # Order pending


@admin.register(PlaylistManga)
class PlaylistMangaAdmin(admin.ModelAdmin):
    """Admin config for PlaylistManga model."""
    search_fields = ["playlist",]
    list_display = ["playlist",]
    list_filter = ["is_watched", "status"]
    list_per_page = 25
    readonly_fields = ["pk",]
    autocomplete_fields = ["manga"]
    ordering = ["pk",]    # Order pending
