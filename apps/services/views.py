from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView

from .models import Services, Projects
from ..blog.models import Blog


class ServicesView(TemplateView):
    template_name = "services.html"

    def get_context_data(self, **kwargs):
        context = {}

        context['architecture'] = get_object_or_404(Services, pk=2)
        context['residential'] = get_object_or_404(Services, pk=3)

        context['architecture_projects'] = Projects.objects.filter(services_project_id=2, main=True, publish=True)
        context['architecture_project1'] = context['architecture_projects'][0]
        context['architecture_project2'] = context['architecture_projects'][1]

        context['residential_projects'] = Projects.objects.filter(services_project_id=3, main=True, publish=True)
        context['residential_project1'] = context['residential_projects'][0]
        context['residential_project2'] = context['residential_projects'][1]
        return context


def single_services(request, slug_service):
    context = {}

    service = get_object_or_404(Services, slug=slug_service)
    context['service'] = service
    projects = service.services_project.all()
    context['projects'] = projects
    projects_main = service.services_project.filter(main=True)
    context['projects_main'] = projects_main
    return render(request, 'service_single.html', context)


def project(request, slug_service, slug_project):
    context = {}

    if Services.objects.filter(slug=slug_service).exists() and Projects.objects.filter(slug=slug_project).exists():
        context['projects'] = Projects.objects.get(slug=slug_project)
    else:
        raise Http404

    return render(request, 'project_single.html', context)
