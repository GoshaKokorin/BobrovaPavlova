from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView

from apps.blog.models import Blog
from apps.services.models import Projects
from apps.services.models import Services


def index(request):
    context = {}

    context['architecture'] = get_object_or_404(Services, pk=2)
    context['residential'] = get_object_or_404(Services, pk=3)

    context['architecture_projects'] = Projects.objects.filter(services_project_id=2, main=True, publish=True)
    context['architecture_project1'] = context['architecture_projects'][0]
    context['architecture_project2'] = context['architecture_projects'][1]

    context['residential_projects'] = Projects.objects.filter(services_project_id=3, main=True, publish=True)
    context['residential_project1'] = context['residential_projects'][0]
    context['residential_project2'] = context['residential_projects'][1]

    context['main_blog'] = get_object_or_404(Blog, main=True)
    context['other_blog'] = Blog.objects.filter(publish=True).order_by('-pk')[:2]
    return render(request, 'index.html', context)


def contact(request):
    context = {}
    return render(request, 'contacts.html', context)


def partners(request):
    context = {}
    return render(request, 'partners.html', context)


class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = {}
        context['main_blog'] = get_object_or_404(Blog, main=True)
        context['other_blog'] = Blog.objects.filter(publish=True).order_by('-pk')[:2]
        return context
