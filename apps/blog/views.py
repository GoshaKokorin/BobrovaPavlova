from django.http import Http404
from django.views.generic.base import TemplateView
from .models import Blog
from django.shortcuts import render


class BlogView(TemplateView):
    template_name = "blog.html"

    def get_context_data(self, **kwargs):
        context = {}
        return context


# class BlogSingleView(TemplateView):
#     query_pk_and_slug = 'slug'
#     template_name = "blog_single.html"
#
#     def get_context_data(self, **kwargs):
#         context = {}
#
#         return context

def blog_single(request, slug_blog):
    context = {}

    if Blog.objects.filter(slug=slug_blog).exists():
        blog = Blog.objects.filter(slug=slug_blog)
        context['blog'] = blog
    else:
        raise Http404

    return render(request, 'blog_single.html', context)
