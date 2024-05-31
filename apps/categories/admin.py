"""Admin for Categories App."""

from django.contrib import admin

from .models import Theme, Demographic


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    """Admin for Theme model."""

    search_fields = [
        "name",
    ]
    list_display = ["name", "available"]
    list_filter = [
        "available",
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
    list_display = ["name", "available"]
    list_filter = [
        "available",
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
