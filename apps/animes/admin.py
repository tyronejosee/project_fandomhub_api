"""Admin for Animes App."""

from django.contrib import admin

from .models import Anime


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
