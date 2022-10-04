from django.contrib import admin
from .models import Services, Projects


@admin.register(Services)
class ServicesFormAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Projects)
class ProjectsFormAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {'slug': ('title',)}
