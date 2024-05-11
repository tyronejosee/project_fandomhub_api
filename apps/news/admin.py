"""Admin for News App."""

from django.contrib import admin

from .models import New


@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    """Admin for New model."""
    search_fields = ["title",]
    list_display = ["title",]
    list_filter = ["available",]
    list_per_page = 25
    readonly_fields = ["pk", "created_at", "updated_at"]
    ordering = ["pk",]
