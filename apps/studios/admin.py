"""Admin for Studios App."""

from django.contrib import admin

from .models import Studio


@admin.register(Studio)
class StudioAdmin(admin.ModelAdmin):
    """Admin for Studio model."""

    ordering = ["created_at"]
    list_per_page = 25
    search_fields = ["name", "name_jpn"]
    list_display = ["name", "available"]
    list_filter = [
        "available",
    ]
    readonly_fields = [
        "pk",
        "slug",
        "created_at",
        "updated_at",
    ]
