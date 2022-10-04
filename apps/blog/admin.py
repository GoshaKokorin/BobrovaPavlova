from django.contrib import admin
from .models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'publish']
    list_editable = ['publish', ]
    prepopulated_fields = {'slug': ('title',)}

