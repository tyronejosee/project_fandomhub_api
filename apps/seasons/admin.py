"""Admin for Seasons App."""

from django.contrib import admin

from .models import Season


@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    """Admin for Season model."""

    list_per_page = 25
    ordering = ["created_at"]
    search_fields = [
        "season",
        "year",
    ]
    list_display = [
        "fullname",
        "available",
    ]
    list_filter = [
        "available",
        "year",
        "season",
    ]
    readonly_fields = [
        "pk",
        "fullname",
        "created_at",
        "updated_at",
    ]
