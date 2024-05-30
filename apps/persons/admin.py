"""Admin for Persons App."""

from django.contrib import admin

from .models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    """Admin for Person model."""

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
        "created_at",
        "updated_at",
    ]
    ordering = [
        "-created_at",
    ]
