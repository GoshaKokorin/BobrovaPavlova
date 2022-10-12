from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateView
from .models import Vacancies
from ..blog.models import Blog


class VacanciesView(TemplateView):
    template_name = "jobs.html"

    def get_context_data(self, **kwargs):
        context = {}

        context['main_blog'] = get_object_or_404(Blog, main=True)
        context['other_blog'] = Blog.objects.filter(publish=True).order_by('-pk')[:2]

        if Vacancies.objects.filter(publish=True).exists():
            context['ready'] = True
            vacancies = Vacancies.objects.filter(publish=True)
            context['vacancies'] = vacancies
        else:
            context['ready'] = False

        return context
