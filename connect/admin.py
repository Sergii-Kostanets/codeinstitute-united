from django.contrib import admin
from .models import Game
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Game)
class GameAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title', 'author'),}
    list_filter = ('status', 'created_on')
    summernote_fields = ('content',)
