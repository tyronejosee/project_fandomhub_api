"""Admin for Genres App."""

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from apps.utils.admin import BaseAdmin
from .models import Genre, Theme, Demographic
from .resources import GenreResource, ThemeResource, DemographicResource


@admin.register(Genre)
class GenreAdmin(ImportExportModelAdmin, BaseAdmin):
    """Admin for Genre model."""

    ordering = ["created_at"]
    search_fields = ["name"]
    list_display = ["name", "is_available"]
    list_filter = ["is_available"]
    readonly_fields = ["pk", "slug", "created_at", "updated_at"]
    resource_class = GenreResource


@admin.register(Theme)
class ThemeAdmin(ImportExportModelAdmin, BaseAdmin):
    """Admin for Theme model."""

    ordering = ["created_at"]
    search_fields = ["name"]
    list_display = ["name", "is_available"]
    list_filter = ["is_available"]
    readonly_fields = ["pk", "slug", "created_at", "updated_at"]
    resource_class = ThemeResource


@admin.register(Demographic)
class DemographicAdmin(ImportExportModelAdmin, BaseAdmin):
    """Admin for Demographic model."""

    search_fields = ["name"]
    list_display = ["name", "is_available"]
    list_filter = ["is_available"]
    readonly_fields = ["pk", "created_at", "updated_at"]
    resource_class = DemographicResource
