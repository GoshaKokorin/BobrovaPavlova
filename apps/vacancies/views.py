from django.views.generic.base import TemplateView
from .models import Vacancies


class VacanciesView(TemplateView):
    template_name = "jobs.html"

    def get_context_data(self, **kwargs):
        context = {}

        if Vacancies.objects.filter(publish=True).exists():
            context['ready'] = True
            vacancies = Vacancies.objects.filter(publish=True)
            context['vacancies'] = vacancies
        else:
            context['ready'] = False

        return context
