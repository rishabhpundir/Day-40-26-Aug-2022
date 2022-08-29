from django.contrib import admin
from .models import Song

# Register your models here.

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['song_title', 'song_duration', 'song_sung_by']


