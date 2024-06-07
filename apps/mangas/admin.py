"""Admin for Mangas App."""

from django.contrib import admin

from .models import Manga


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
        "is_available",
    ]
    list_filter = [
        "status",
        "genres",
    ]
    list_editable = [
        "is_available",
    ]
    readonly_fields = [
        "pk",
        "slug",
        "score",
        "ranked",
        "popularity",
        "members",
        "favorites",
        "created_at",
        "updated_at",
    ]
    autocomplete_fields = [
        "author_id",
        "demographic_id",
        "serialization_id",
        "genres",
        "themes",
    ]
