"""Admin for News App."""

from django.contrib import admin

from apps.utils.admin import BaseAdmin
from .models import News


@admin.register(News)
class NewsAdmin(BaseAdmin):
    """Admin for News model."""

    ordering = ["-created_at"]
    search_fields = ["name"]
    list_display = ["name", "is_available"]
    list_filter = ["is_available"]
    readonly_fields = ["pk", "created_at", "updated_at"]
    filter_horizontal = ["anime_relations", "manga_relations"]
