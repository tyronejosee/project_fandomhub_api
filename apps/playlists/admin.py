"""Admin for Playlists App."""

from django.contrib import admin
from apps.playlists.models import Playlist, PlaylistAnime, PlaylistManga

admin.site.register(Playlist)
admin.site.register(PlaylistAnime)
admin.site.register(PlaylistManga)


# """Admin for Watchlists App."""

# from django.contrib import admin
# from apps.watchlists.models import AnimeWatchlist, MangaWatchlist


# @admin.register(AnimeWatchlist)
# class AnimeWatchlistAdmin(admin.ModelAdmin):
#     """Admin config for AnimeWatchlist model."""
#     search_fields = ["user",]
#     list_display = ["user", "anime"]
#     list_filter = ["is_watched",]
#     list_per_page = 25
#     readonly_fields = ["pk",]
#     ordering = ["pk",]


# @admin.register(MangaWatchlist)
# class MangaWatchlistAdmin(admin.ModelAdmin):
#     """Admin config for MangaWatchlist model."""
#     search_fields = ["user",]
#     list_display = ["user", "manga"]
#     list_filter = ["is_watched",]
#     list_per_page = 25
#     readonly_fields = ["pk",]
#     ordering = ["pk",]
