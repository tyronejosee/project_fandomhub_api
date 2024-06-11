"""Admin for News App."""

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from apps.utils.admin import BaseAdmin
from .models import News
from .resources import NewsResource


@admin.register(News)
class NewsAdmin(ImportExportModelAdmin, BaseAdmin):
    """Admin for News model."""

    ordering = ["-created_at"]
    search_fields = ["name"]
    filter_horizontal = ["anime_relations", "manga_relations"]
    list_display = ["name", "is_available"]
    list_filter = ["is_available"]
    readonly_fields = ["pk", "created_at", "updated_at"]
    resource_class = NewsResource
