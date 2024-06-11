"""Admin for Mangas App."""

from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from apps.utils.admin import BaseAdmin
from apps.utils.models import Picture
from .models import Manga, Magazine


class PictureInline(GenericTabularInline):
    model = Picture


@admin.register(Magazine)
class MagazineAdmin(BaseAdmin):
    """Admin for Magazine model."""

    search_fields = ["name"]
    list_display = ["name", "count", "is_available"]


@admin.register(Manga)
class MangaAdmin(BaseAdmin):
    """Admin for Manga model."""

    search_fields = ["name", "name_jpn", "name_rom"]
    list_display = ["name", "is_available"]
    list_filter = ["status", "genres"]
    list_editable = ["is_available"]
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
    autocomplete_fields = ["author_id", "demographic_id", "serialization_id"]
    filter_horizontal = ["genres", "themes"]
    inlines = [PictureInline]
