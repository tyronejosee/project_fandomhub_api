"""Admin for Contents App."""

from django.contrib import admin
from django.utils.translation import gettext as _
from apps.categories.models import Studio, Genre, Season, Url, Author, Demographic


@admin.register(Url)
class UrlAdmin(admin.ModelAdmin):
    """Admin config for Url model."""
    search_fields = ('tag', 'url')
    list_display = ('url', 'tag', 'available')
    list_filter = ('available',)
    list_per_page = 25
    readonly_fields = ('pk', 'created_at', 'updated_at',)
    ordering = ('pk',)


@admin.register(Studio)
class StudioAdmin(admin.ModelAdmin):
    """Admin config for Studio model."""
    search_fields = ('name', 'name_jpn')
    list_display = ('name', 'available')
    list_filter = ('available',)
    list_per_page = 25
    readonly_fields = ('pk', 'created_at', 'updated_at',)
    ordering = ('pk',)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Admin config for Genre model."""
    search_fields = ('name',)
    list_display = ('name', 'available')
    list_filter = ('available',)
    list_per_page = 25
    readonly_fields = ('pk', 'created_at', 'updated_at',)
    ordering = ('pk',)


@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    """Admin config for Season model."""
    search_fields = ('season', 'year')
    list_display = ('season', 'available')
    list_filter = ('available',)
    list_per_page = 25
    readonly_fields = ('pk', 'created_at', 'updated_at',)
    ordering = ('pk',)


@admin.register(Demographic)
class DemographicAdmin(admin.ModelAdmin):
    """Admin config for Demographic model."""
    search_fields = ('name',)
    list_display = ('name', 'available')
    list_filter = ('available',)
    list_per_page = 25
    readonly_fields = ('pk', 'created_at', 'updated_at',)
    ordering = ('pk',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """Admin config for Author model."""
    search_fields = ('name',)
    list_display = ('name', 'available')
    list_filter = ('available',)
    list_per_page = 25
    readonly_fields = ('pk', 'created_at', 'updated_at',)
    ordering = ('pk',)
