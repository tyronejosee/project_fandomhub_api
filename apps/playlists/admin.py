"""Admin for Playlists App."""

from django.contrib import admin
from apps.playlists.models import Playlist, PlaylistItem


@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    """Admin config for Playlist model."""
    search_fields = ["user",]
    list_display = ["user",]
    list_per_page = 25
    readonly_fields = ["pk",]
    ordering = ["pk",]


@admin.register(PlaylistItem)
class PlaylistItemAdmin(admin.ModelAdmin):
    """Admin config for PlaylistItem model."""
    search_fields = ["playlist",]
    list_display = ["playlist",]
    list_filter = ["is_watched", "status"]
    list_per_page = 25
    readonly_fields = ["pk",]
    ordering = ["pk",]    # Order pending
