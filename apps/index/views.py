import requests
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView
from apps.index.forms import IndexForms


# class IndexView(TemplateView):
#     template_name = "index.html"
#
#     if request.method == 'POST':
#         form = ProfileForm(request.POST, instance=profile)
#         if form.is_valid():
#             form.save()
#
#             context['first_name'] = form['first_name'].value()
#             context['last_name'] = form['last_name'].value()
#             context['email'] = form['email'].value()
#             context['company'] = form['company'].value()
#             context['address'] = form['address'].value()
#             context['phone'] = form['phone'].value()
#             context['city'] = form['city'].value()
#             context['zip'] = form['zip'].value()
#             context['country'] = form['country'].value()
#
#             context['form'] = ProfileForm(instance=profile)
#             return render(request, 'wineservice/checkout/checkout-step-2.html', context)
#
#     context['form'] = ProfileForm(instance=profile)
#
#     def get_context_data(self, **kwargs):
#         context = {}
#         return context


def index(request):
    context = {}

    if request.method == 'POST':
        form = IndexForms(request.POST)
        if form.is_valid():
            form.save()
            context['name'] = form['name'].value()
            context['phone'] = form['phone'].value()
            context['form'] = IndexForms()
            # name = form.cleaned_data['name']
            # return JsonResponse({"name": name}, status=200)
        else:
            errors = form.errors.as_json()
            # return JsonResponse({"errors": errors}, status=400)
    else:
        context['form'] = IndexForms()
    return render(request, 'index.html', context)


class ContactsView(TemplateView):
    template_name = "contacts.html"

    def get_context_data(self, **kwargs):
        context = {}
        return context


class BlogView(TemplateView):
    template_name = "blog.html"

    def get_context_data(self, **kwargs):
        context = {}
        return context


class PartnersView(TemplateView):
    template_name = "partners.html"

    def get_context_data(self, **kwargs):
        context = {}
        return context


class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = {}
        return context


class BlogSingleView(TemplateView):
    template_name = "blog_single.html"

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
