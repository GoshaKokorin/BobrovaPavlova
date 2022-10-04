from django.views.generic.base import TemplateView


class BlogView(TemplateView):
    template_name = "blog.html"

    def get_context_data(self, **kwargs):
        context = {}
        return context


class BlogSingleView(TemplateView):
    template_name = "blog_single.html"

    def get_context_data(self, **kwargs):
        context = {}
        return context
