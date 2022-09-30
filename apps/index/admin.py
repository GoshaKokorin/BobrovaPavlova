from django.contrib import admin
from .models import IndexForm


@admin.register(IndexForm)
class IndexFormAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'сhecked']
    list_editable = ['сhecked', ]
