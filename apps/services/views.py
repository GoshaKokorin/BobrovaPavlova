from django.views.generic.base import TemplateView


class ServicesView(TemplateView):
    template_name = "services.html"

    def get_context_data(self, **kwargs):
        context = {}
        return context
