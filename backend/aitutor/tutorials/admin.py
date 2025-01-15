from django.contrib import admin
from .models import Language, Manual, Topic, Tutorial

# Register your models here.

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Manual)
class ManualAdmin(admin.ModelAdmin):
    list_display = ('name', 'language', 'publication_date')
    list_filter = ('language', 'publication_date')
    search_fields = ('name', 'language__name')
    autocomplete_fields = ['language']

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'manual')
    list_filter = ('manual',)
    search_fields = ('name', 'manual__name')
    autocomplete_fields = ['manual']

@admin.register(Tutorial)
class TutorialAdmin(admin.ModelAdmin):
    list_display = ('name', 'topic', 'publication_date')
    list_filter = ('topic', 'publication_date')
    search_fields = ('name', 'content', 'topic__name')
    autocomplete_fields = ['topic']
