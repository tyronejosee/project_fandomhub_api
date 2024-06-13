"""Admin for Persons App."""

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from apps.utils.admin import BaseAdmin
from .models import Person, StaffAnime
from .resources import PersonResource, StaffAnimeResource


@admin.register(Person)
class PersonAdmin(ImportExportModelAdmin, BaseAdmin):
    """Admin for Person model."""

    ordering = ["-created_at"]
    search_fields = ["name"]
    list_display = ["name", "category", "age", "is_available"]
    list_filter = ["is_available", "category"]
    readonly_fields = ["pk", "slug", "created_at", "updated_at"]
    resource_class = PersonResource

    @admin.display(description="Age")
    def get_age(self, obj):
        return obj.age


@admin.register(StaffAnime)
class StaffAnimeAdmin(ImportExportModelAdmin, BaseAdmin):
    """Admin for StaffAnime model."""

    search_fields = ["person_id", "anime_id"]
    list_display = ["person_id", "anime_id", "is_available"]
    list_filter = ["anime_id"]
    list_editable = ["is_available"]
    readonly_fields = ["pk", "created_at", "updated_at"]
    resource_class = StaffAnimeResource
