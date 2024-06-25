"""Admin for Mangas App."""

from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from import_export.admin import ImportExportModelAdmin

from apps.utils.admin import BaseAdmin
from apps.utils.models import Picture
from .models import Magazine, Manga, MangaStats
from .resources import MagazineResource, MangaResource, MangaStatsResource


class PictureInline(GenericTabularInline):
    model = Picture


@admin.register(Magazine)
class MagazineAdmin(ImportExportModelAdmin, BaseAdmin):
    """Admin for Magazine model."""

    search_fields = ["name"]
    list_display = ["name", "count", "is_available"]
    resource_class = MagazineResource


@admin.register(Manga)
class MangaAdmin(ImportExportModelAdmin, BaseAdmin):
    """Admin for Manga model."""

    search_fields = ["name", "name_jpn", "name_rom"]
    list_display = ["name", "is_available"]
    list_filter = ["status", "genres"]
    list_editable = ["is_available"]
    readonly_fields = [
        "pk",
        "slug",
        "created_at",
        "updated_at",
    ]
    autocomplete_fields = ["author_id", "demographic_id", "serialization_id"]
    filter_horizontal = ["genres", "themes"]
    inlines = [PictureInline]
    resource_class = MangaResource


@admin.register(MangaStats)
class MangaStatsAdmin(ImportExportModelAdmin, BaseAdmin):
    """Admin for MangaStats model."""

    search_fields = ["name", "name_jpn", "name_rom"]
    list_display = [
        "manga_id",
        "reading",
        "completed",
        "on_hold",
        "dropped",
        "plan_to_read",
        "total",
        "is_available",
    ]
    list_editable = ["is_available"]
    readonly_fields = ["pk", "created_at", "updated_at"]
    resource_class = MangaStatsResource
