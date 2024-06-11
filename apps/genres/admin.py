"""Admin for Genres App."""

from django.contrib import admin

from apps.utils.admin import BaseAdmin
from .models import Genre, Theme, Demographic


@admin.register(Genre)
class GenreAdmin(BaseAdmin):
    """Admin for Genre model."""

    ordering = ["created_at"]
    search_fields = ["name"]
    list_display = ["name", "is_available"]
    list_filter = ["is_available"]
    readonly_fields = ["pk", "slug", "created_at", "updated_at"]


@admin.register(Theme)
class ThemeAdmin(BaseAdmin):
    """Admin for Theme model."""

    ordering = ["created_at"]
    search_fields = ["name"]
    list_display = ["name", "is_available"]
    list_filter = ["is_available"]
    readonly_fields = ["pk", "slug", "created_at", "updated_at"]


@admin.register(Demographic)
class DemographicAdmin(BaseAdmin):
    """Admin for Demographic model."""

    search_fields = ["name"]
    list_display = ["name", "is_available"]
    list_filter = ["is_available"]
    readonly_fields = ["pk", "created_at", "updated_at"]
