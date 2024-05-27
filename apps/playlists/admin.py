"""Admin for Playlists App."""

from django.contrib import admin

from .models import Playlist, PlaylistItem


@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    """Admin for Playlist model."""

    list_per_page = 25
    search_fields = [
        "user",
    ]
    list_display = [
        "user",
    ]
    readonly_fields = [
        "pk",
    ]
    ordering = [
        "created_at",
    ]


@admin.register(PlaylistItem)
class PlaylistItemAdmin(admin.ModelAdmin):
    """Admin for PlaylistItem model."""

    list_per_page = 25
    search_fields = [
        "playlist",
    ]
    list_display = [
        "playlist",
        "content_type",
    ]
    readonly_fields = [
        "pk",
        "created_at",
        "updated_at",
    ]
    ordering = [
        "created_at",
    ]
