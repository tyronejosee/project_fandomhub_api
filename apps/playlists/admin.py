"""Admin for Playlists App."""

from django.contrib import admin

from .models import Playlist


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
