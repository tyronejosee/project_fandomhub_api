"""Admin for Contents App."""

from django.contrib import admin
from django.utils.translation import gettext as _
from apps.contents.models import Anime, Manga


@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    """Admin config for Anime model."""
    search_fields = ('name', 'name_jpn')
    list_display = ('name', 'available')
    list_filter = ('status', 'genre_id', 'studio_id')
    list_editable = ('available',)
    list_per_page = 25
    readonly_fields = ('pk', 'created_at', 'updated_at',)
    ordering = ('pk',)


@admin.register(Manga)
class MangaAdmin(admin.ModelAdmin):
    """Admin config for Manga model."""
    search_fields = ('name', 'name_jpn')
    list_display = ('name', 'available')
    list_filter = ('status', 'genre_id',)
    list_editable = ('available',)
    list_per_page = 25
    readonly_fields = ('pk', 'created_at', 'updated_at',)
    ordering = ('pk',)
