from django.views.generic.base import TemplateView


class ServicesView(TemplateView):
    template_name = "services.html"

    def get_context_data(self, **kwargs):
        context = {}
        return context


class ArhView(TemplateView):
    template_name = "architecture.html"

    def get_context_data(self, **kwargs):
        context = {}
        return context


class JilView(TemplateView):
    template_name = "residential.html"

    def get_context_data(self, **kwargs):
        context = {}
        return context


class KomView(TemplateView):
    template_name = "commercial.html"

    def get_context_data(self, **kwargs):
        context = {}
        return context


class ProjectView(TemplateView):
    template_name = "project_single.html"

    def get_context_data(self, **kwargs):
        context = {}
        return context
