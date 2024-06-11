"""Admin for Producers App."""

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from apps.utils.admin import BaseAdmin
from .models import Producer
from .resources import ProducerResource


@admin.register(Producer)
class ProducerAdmin(ImportExportModelAdmin, BaseAdmin):
    """Admin for Producer model."""

    ordering = ["created_at"]
    search_fields = ["name", "name_jpn"]
    list_display = ["name", "is_available"]
    list_filter = ["is_available"]
    readonly_fields = ["pk", "slug", "created_at", "updated_at"]
    resource_class = ProducerResource
