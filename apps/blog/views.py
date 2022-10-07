from django.http import Http404
from django.views.generic.base import TemplateView
from .models import Blog
from django.shortcuts import render, get_object_or_404


class BlogView(TemplateView):
    template_name = "blog.html"

    def get_context_data(self, **kwargs):
        context = {}
        context['main_blog'] = get_object_or_404(Blog, main=True)

        return context


def blog_single(request, slug_blog):
    context = {}
    context['item'] = get_object_or_404(Blog, slug=slug_blog)

    return render(request, 'blog_single.html', context)
