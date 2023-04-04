from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'publish']
    list_editable = ['publish', ]
    prepopulated_fields = {'slug': ('title',)}
