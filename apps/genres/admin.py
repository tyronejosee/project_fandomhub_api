"""Admin for Genres App."""

from django.contrib import admin

from .models import Genre


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
        "available",
    ]
    list_filter = [
        "available",
    ]
    readonly_fields = [
        "pk",
        "slug",
        "created_at",
        "updated_at",
    ]
