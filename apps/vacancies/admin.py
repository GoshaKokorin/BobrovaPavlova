from django.contrib import admin
from .models import Vacancies


@admin.register(Vacancies)
class VacanciesAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'publish']
    list_editable = ['publish', ]
    prepopulated_fields = {'slug': ('title',)}