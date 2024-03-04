"""Admin for Contents App."""

from django.contrib import admin
from apps.categories.models import Studio, Genre, Theme, Season, Demographic


@admin.register(Studio)
class StudioAdmin(admin.ModelAdmin):
    """Admin config for Studio model."""
    search_fields = ["name", "name_jpn"]
    list_display = ["name", "available"]
    list_filter = ["available",]
    list_per_page = 25
    readonly_fields = ["pk", "slug", "created_at", "updated_at",]
    ordering = ["pk",]


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Admin config for Genre model."""
    search_fields = ["name",]
    list_display = ["name", "available"]
    list_filter = ["available",]
    list_per_page = 25
    readonly_fields = ["pk", "slug", "created_at", "updated_at",]
    ordering = ["pk",]


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    """Admin config for Theme model."""
    search_fields = ["name",]
    list_display = ["name", "available"]
    list_filter = ["available",]
    list_per_page = 25
    readonly_fields = ["pk", "slug", "created_at", "updated_at",]
    ordering = ["pk",]


@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    """Admin config for Season model."""
    search_fields = ["season", "year"]
    list_display = ["fullname", "available"]
    list_filter = ["available", "year", "season"]
    list_per_page = 25
    readonly_fields = ["pk", "fullname", "created_at", "updated_at",]
    ordering = ["pk",]


@admin.register(Demographic)
class DemographicAdmin(admin.ModelAdmin):
    """Admin config for Demographic model."""
    search_fields = ["name",]
    list_display = ["name", "available"]
    list_filter = ["available",]
    list_per_page = 25
    readonly_fields = ["pk", "created_at", "updated_at",]
    ordering = ["pk",]
