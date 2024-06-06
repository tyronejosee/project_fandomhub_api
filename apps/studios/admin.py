"""Admin for Studios App."""

from django.contrib import admin

from .models import Studio


@admin.register(Studio)
class StudioAdmin(admin.ModelAdmin):
    """Admin for Studio model."""

    list_per_page = 25
    ordering = ["created_at"]
    search_fields = [
        "name",
        "name_jpn",
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
