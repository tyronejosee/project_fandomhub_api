"""Admin for Utils App."""

from django.contrib import admin
from django.utils.translation import gettext as _
from import_export.admin import ImportExportModelAdmin

from .models import Picture, Video
from .resources import PictureResource, VideoResource


class BaseAdmin(admin.ModelAdmin):
    """Base Admin."""

    list_per_page = 25
    date_hierarchy = "created_at"
    # empty_value_display = "pending"
    # save_on_top = True
    actions = ["soft_delete", "restore_items"]

    @admin.action(description=_("Soft delete selected items"))
    def soft_delete(self, request, queryset):
        """Action to perform soft delete by setting is_available to False."""
        queryset.update(is_available=False)

    @admin.action(description=_("Restore selected items"))
    def restore_items(self, request, queryset):
        """Action to restore items by setting is_available to True."""
        queryset.update(is_available=True)


@admin.register(Picture)
class PictureAdmin(ImportExportModelAdmin, BaseAdmin):
    """Admin for Picture model."""

    search_fields = ["name", "object_id"]
    list_display = ["name", "image", "content_type"]
    list_filter = ["is_available"]
    readonly_fields = ["pk", "created_at", "updated_at"]
    resource_class = PictureResource


@admin.register(Video)
class VideoAdmin(ImportExportModelAdmin, BaseAdmin):
    """Admin for Video model."""

    search_fields = ["object_id"]
    list_display = ["object_id", "content_type"]
    list_filter = ["is_available"]
    readonly_fields = ["pk", "created_at", "updated_at"]
    resource_class = VideoResource
