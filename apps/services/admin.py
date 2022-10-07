from django.contrib import admin
from .models import *


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {'slug': ('title',)}
