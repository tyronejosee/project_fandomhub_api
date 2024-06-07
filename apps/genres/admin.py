"""Admin for Genres App."""

from django.contrib import admin

from .models import Genre, Theme, Demographic


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Admin for Genre model."""

    ordering = ["created_at"]
    list_per_page = 25
    search_fields = [
        "name",
    ]
    list_display = [
        "name",
        "is_available",
    ]
    list_filter = [
        "is_available",
    ]
    readonly_fields = [
        "pk",
        "slug",
        "created_at",
        "updated_at",
    ]


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    """Admin for Theme model."""

    search_fields = [
        "name",
    ]
    list_display = ["name", "is_available"]
    list_filter = [
        "is_available",
    ]
    list_per_page = 25
    readonly_fields = [
        "pk",
        "slug",
        "created_at",
        "updated_at",
    ]
    ordering = [
        "created_at",
    ]


@admin.register(Demographic)
class DemographicAdmin(admin.ModelAdmin):
    """Admin for Demographic model."""

    search_fields = [
        "name",
    ]
    list_display = ["name", "is_available"]
    list_filter = [
        "is_available",
    ]
    list_per_page = 25
    readonly_fields = [
        "pk",
        "created_at",
        "updated_at",
    ]
    ordering = [
        "pk",
    ]
