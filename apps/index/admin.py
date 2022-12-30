from django.contrib import admin
from django.contrib.auth.models import Group, User

from .models import IndexForm, PartnersForm


@admin.register(IndexForm)
class IndexFormAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'сhecked']
    list_editable = ['сhecked', ]


@admin.register(PartnersForm)
class PartnersFormAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'сhecked']
    list_editable = ['сhecked', ]


admin.site.unregister(Group)
admin.site.unregister(User)

