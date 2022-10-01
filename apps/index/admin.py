from django.contrib import admin
from .models import IndexForm, PartnersForm


@admin.register(IndexForm)
class IndexFormAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'сhecked']
    list_editable = ['сhecked', ]


@admin.register(PartnersForm)
class PartnersFormAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'сhecked']
    list_editable = ['сhecked', ]
