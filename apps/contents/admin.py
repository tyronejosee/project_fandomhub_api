"""Admin for Contents App."""

from django.contrib import admin
from django.utils.translation import gettext as _
from apps.contents.models import (
    Content,
    Studio,
    Genre,
    Premiered,
    Rating,
    Url
)


@admin.register(Url)
class UrlAdmin(admin.ModelAdmin):
    """Admin config for Url model."""
    search_fields = ('tag',)
    list_display = ('tag', 'url', 'available')
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


@admin.register(Premiered)
class PremieredAdmin(admin.ModelAdmin):
    """Admin config for Premiered model."""
    search_fields = ('name',)
    list_display = ('name', 'available')
    list_filter = ('available',)
    list_per_page = 25
    readonly_fields = ('pk', 'created_at', 'updated_at',)
    ordering = ('pk',)


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """Admin config for Rating model."""
    search_fields = ('name',)
    list_display = ('name', 'available')
    list_filter = ('available',)
    list_per_page = 25
    readonly_fields = ('pk', 'created_at', 'updated_at',)
    ordering = ('pk',)


@admin.register(Content)
class UserAdmin(admin.ModelAdmin):
    """Admin config for Content model."""
    search_fields = ('name', 'name_jpn')
    list_display = ('name', 'available')
    list_filter = ('status', 'genre_id', 'studio_id')
    list_editable = ('available',)
    list_per_page = 25
    readonly_fields = ('pk', 'created_at', 'updated_at',)
    ordering = ('pk',)
