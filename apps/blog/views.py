from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView

from apps.blog.models import Blog


class BlogView(TemplateView):
    template_name = "404.html"

    def get_context_data(self, **kwargs):
        context = {'main_blog': get_object_or_404(Blog, main=True)}

        return context


def blog_single(request, slug_blog):
    context = {'item': get_object_or_404(Blog, slug=slug_blog)}

    return render(request, '404.html', context)
