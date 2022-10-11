from django.http import Http404, HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.shortcuts import render, get_object_or_404

from .models import Services, Projects
from ..blog.models import Blog


# TODO: пофиксить вывод проектов в любой услуге

class ServicesView(TemplateView):
    template_name = "services.html"

    def get_context_data(self, **kwargs):
        context = {}
        service = Services.objects.all()
        context['service'] = service

        # try:
        #     context['architecture'] = get_object_or_404(Services, id=2)
        # except:
        #     return HttpResponseRedirect('/error')
        #
        # try:
        #     context['residential'] = get_object_or_404(Services, id=3)
        # except:
        #     return HttpResponseRedirect('/error')
        #
        # try:
        #     context['commercial'] = get_object_or_404(Services, id=4)
        # except:
        #     return HttpResponseRedirect('/error')

        context['architecture'] = get_object_or_404(Services, pk=2)
        context['residential'] = get_object_or_404(Services, pk=3)
        context['commercial'] = get_object_or_404(Services, pk=4)

        context['main_blog'] = get_object_or_404(Blog, main=True)
        context['other_blog'] = Blog.objects.filter(publish=True).order_by('-pk')[:2]

        return context


def single_services(request, slug_service):
    context = {}

    service = get_object_or_404(Services, slug=slug_service)
    context['service'] = service
    projects = service.services_project.all()
    context['projects'] = projects
    projects_main = service.services_project.filter(main=True)
    context['projects_main'] = projects_main

    context['main_blog'] = get_object_or_404(Blog, main=True)
    context['other_blog'] = Blog.objects.filter(publish=True).order_by('-pk')[:2]

    return render(request, 'service_single.html', context)


def project(request, slug_service, slug_project):
    context = {}

    if Services.objects.filter(slug=slug_service).exists() and Projects.objects.filter(slug=slug_project).exists():
        projects = Projects.objects.get(slug=slug_project)
        context['projects'] = projects
    else:
        raise Http404

    return render(request, 'project_single.html', context)
