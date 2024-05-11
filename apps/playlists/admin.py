"""Admin for Playlists App."""

from django.contrib import admin

from .models import Playlist, PlaylistAnime, PlaylistManga


@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    """Admin for Playlist model."""
    search_fields = ["user",]
    list_display = ["user",]
    list_per_page = 25
    readonly_fields = ["pk",]
    ordering = ["created_at",]


@admin.register(PlaylistAnime)
class PlaylistAnimeAdmin(admin.ModelAdmin):
    """Admin for PlaylistAnime model."""
    search_fields = ["playlist",]
    list_display = ["playlist", "anime"]
    list_filter = ["is_watched", "status"]
    list_per_page = 25
    readonly_fields = ["pk",]
    autocomplete_fields = ["anime"]
    ordering = ["created_at",]    # Order pending


@admin.register(PlaylistManga)
class PlaylistMangaAdmin(admin.ModelAdmin):
    """Admin for PlaylistManga model."""
    search_fields = ["playlist",]
    list_display = ["playlist", "manga"]
    list_filter = ["is_watched", "status"]
    list_per_page = 25
    readonly_fields = ["pk",]
    autocomplete_fields = ["manga"]
    ordering = ["created_at",]    # Order pending
