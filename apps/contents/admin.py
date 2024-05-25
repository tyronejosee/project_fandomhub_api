"""Admin for Contents App."""

from django.contrib import admin

from .models import Anime, Manga


@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    """Admin for Anime model."""

    list_per_page = 25
    search_fields = [
        "name",
        "name_jpn",
        "name_rom",
    ]
    list_display = [
        "name",
        "available",
    ]
    list_filter = [
        "status",
        "genres",
        "studio",
    ]
    list_editable = [
        "available",
    ]
    readonly_fields = [
        "pk",
        "slug",
        "mean",
        "rank",
        "popularity",
        "favorites",
        "num_list_users",
        "created_at",
        "updated_at",
    ]
    autocomplete_fields = [
        "studio",
        "genres",
        "themes",
        "season",
    ]


@admin.register(Manga)
class MangaAdmin(admin.ModelAdmin):
    """Admin for Manga model."""

    list_per_page = 25
    search_fields = [
        "name",
        "name_jpn",
        "name_rom",
    ]
    list_display = [
        "name",
        "available",
    ]
    list_filter = [
        "status",
        "genres",
    ]
    list_editable = [
        "available",
    ]
    readonly_fields = [
        "pk",
        "slug",
        "mean",
        "rank",
        "popularity",
        "num_list_users",
        "favorites",
        "created_at",
        "updated_at",
    ]
    autocomplete_fields = [
        "author",
        "demographic",
        "genres",
        "themes",
    ]
