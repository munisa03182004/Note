from django.contrib import admin

from . models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    search_fields = ['title','body']
    list_filter = ['created','updated']
    list_display = ['title','is_done']
    list_display_links = ['title']
    list_editable = ['is_done']
    list_per_page = 100
    ordering = ['created','updated','title']
    save_on_top = True