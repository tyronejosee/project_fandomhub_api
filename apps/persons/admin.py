"""Admin for Persons App."""

from django.contrib import admin

from .models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    """Admin for Person model."""

    ordering = ["-created_at"]
    list_per_page = 25
    search_fields = [
        "name",
    ]
    list_display = [
        "name",
        "category",
        "available",
    ]
    list_filter = [
        "available",
        "category",
    ]
    readonly_fields = [
        "pk",
        "slug",
        "created_at",
        "updated_at",
    ]
