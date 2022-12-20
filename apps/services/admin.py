from django.contrib import admin
from .models import *


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ['title', 'pk']
    prepopulated_fields = {'slug': ('title',)}
    # exclude = ('slug',)


@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {'slug': ('title',)}
