"""Admin for Utils App."""

from django.contrib import admin

from .models import Picture


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    """Admin for Picture model."""

    list_per_page = 25
    search_fields = [
        "object_id",
    ]
    list_display = [
        "object_id",
        "content_type",
    ]
    list_filter = [
        "available",
    ]
    readonly_fields = [
        "pk",
        "created_at",
        "updated_at",
    ]
