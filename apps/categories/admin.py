"""Admin for Contents App."""

from django.contrib import admin
from apps.categories.models import Studio, Genre, Season, Demographic


@admin.register(Studio)
class StudioAdmin(admin.ModelAdmin):
    """Admin config for Studio model."""
    search_fields = ["name", "name_jpn"]
    list_display = ["name", "available"]
    list_filter = ["available",]
    list_per_page = 25
    readonly_fields = ["pk", "created_at", "updated_at",]
    ordering = ["pk",]


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Admin config for Genre model."""
    search_fields = ["name",]
    list_display = ["name", "available"]
    list_filter = ["available",]
    list_per_page = 25
    readonly_fields = ["pk", "created_at", "updated_at",]
    ordering = ["pk",]


@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    """Admin config for Season model."""
    search_fields = ["season", "year"]
    list_display = ["season", "available"]
    list_filter = ["available",]
    list_per_page = 25
    readonly_fields = ["pk", "created_at", "updated_at",]
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
