"""Admin for News App."""

from django.contrib import admin

from .models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    """Admin for News model."""

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
    ordering = [
        "-created_at",
        "pk",
    ]
