from django.contrib import admin
from .models import Game
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Game)
class GameAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'platform', 'status', 'created_on')
    search_fields = ('title', 'platform', 'content')
    prepopulated_fields = {'slug': ('title',),}
    list_filter = ('status', 'platform', 'created_on')
    summernote_fields = ('content',)

    fieldsets = (
        ('Header', {
            'fields': ('title', 'slug', 'platform', 'excerpt',)
        }),
        ('Main', {
            'fields': ('content',),
        }),
        ('Additional', {
            'fields': ('featured_image',),
        }),
        ('Publish', {
            'fields': ('status',),
        }),
    )
