"""Admin for News App."""

from django.contrib import admin

from .models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    """Admin for News model."""

    ordering = [
        "-created_at",
    ]
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
        "created_at",
        "updated_at",
    ]
    filter_horizontal = [
        "anime_relations",
        "manga_relations",
    ]
