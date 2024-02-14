"""Admin for Persons App."""

from django.contrib import admin
from apps.persons.models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """Admin config for Author model."""
    search_fields = ('name',)
    #list_display = ('name', 'available')
    #list_filter = ('available',)
    list_per_page = 25
    readonly_fields = ('pk',)
    ordering = ('pk',)
