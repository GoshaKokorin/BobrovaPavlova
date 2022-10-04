from django.contrib import admin
from .models import *


class RequirementsAdmin(admin.TabularInline):
    model = Requirements
    extra = 0


class CircumstancesAdmin(admin.TabularInline):
    model = Circumstances
    extra = 0


class ResponsibilitiesAdmin(admin.TabularInline):
    model = Responsibilities
    extra = 0


@admin.register(Vacancies)
class VacanciesAdmin(admin.ModelAdmin):
    list_display = ['title', 'publish']
    list_editable = ['publish', ]
    inlines = [ResponsibilitiesAdmin, RequirementsAdmin, CircumstancesAdmin]

