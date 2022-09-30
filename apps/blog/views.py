from django.views.generic.base import TemplateView


class BlogView(TemplateView):
    template_name = "error.html"

    def get_context_data(self, **kwargs):
        context = {}
        return context


class BlogSingleView(TemplateView):
    template_name = "error.html"

    def get_context_data(self, **kwargs):
        context = {}
        return context
