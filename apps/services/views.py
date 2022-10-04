from django.http import Http404
from django.views.generic.base import TemplateView
from .models import Services
from django.shortcuts import render


class ServicesView(TemplateView):
    template_name = "services.html"

    def get_context_data(self, **kwargs):
        context = {}
        service = Services.objects.all()
        context['service'] = service

        return context


def single_services(request, slug_service):
    context = {}

    if Services.objects.filter(slug=slug_service).exists():
        service = Services.objects.filter(slug=slug_service)
        context['service'] = service
    else:
        raise Http404

    return render(request, 'service_single.html', context)


def project(request, slug_service, slug_project):
    context = {}

    if Services.objects.filter(slug=slug_service).exists():
        service = Services.objects.filter(slug=slug_service)
        context['service'] = service
    else:
        raise Http404

    return render(request, 'service_single.html', context)


class ProjectView(TemplateView):
    template_name = "services.html"

    def get_context_data(self, **kwargs):
        context = {}
        return context


class ArhView(TemplateView):
    template_name = "projects/service_single.html"

    def get_context_data(self, **kwargs):
        context = {}
        return context


class JilView(TemplateView):
    template_name = "projects/service_single_living.html"

    def get_context_data(self, **kwargs):
        context = {}
        return context


class KomView(TemplateView):
    template_name = "projects/service_single_commerce.html"

    def get_context_data(self, **kwargs):
        context = {}
        return context


class Project1View(TemplateView):
    template_name = "projects/project_single_east_legend.html"

    def get_context_data(self, **kwargs):
        context = {}
        return context


class Project2View(TemplateView):
    template_name = "projects/project_single_itmo.html"

    def get_context_data(self, **kwargs):
        context = {}
        return context


class Project3View(TemplateView):
    template_name = "projects/project_single_market.html"

    def get_context_data(self, **kwargs):
        context = {}
        return context


class Project4View(TemplateView):
    template_name = "projects/project_single_mogaisky.html"

    def get_context_data(self, **kwargs):
        context = {}
        return context


class Project5View(TemplateView):
    template_name = "projects/project_single_sosnovka.html"

    def get_context_data(self, **kwargs):
        context = {}
        return context


class Project6View(TemplateView):
    template_name = "projects/project_single_strelna.html"

    def get_context_data(self, **kwargs):
        context = {}
        return context


class Project7View(TemplateView):
    template_name = "projects/project_single.html"

    def get_context_data(self, **kwargs):
        context = {}
        return context
