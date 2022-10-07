from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from apps.index.forms import IndexForms, PartnersForms
from apps.services.models import Services
from apps.blog.models import Blog


def index(request):
    context = {}

    context['architecture'] = Services.objects.get(id=2)
    context['residential'] = Services.objects.get(id=3)
    context['commercial'] = Services.objects.get(id=4)

    if request.method == 'POST':
        form = IndexForms(request.POST)
        if form.is_valid():
            form.save()
            context['name'] = form['name'].value()
            context['phone'] = form['phone'].value()
            context['form'] = IndexForms()
            # name = form.cleaned_data['name']
            # return render(request, 'about.html', context)
        else:
            errors = form.errors.as_json()
            # return JsonResponse({"errors": errors}, status=400)
    else:
        context['form'] = IndexForms()

    context['main_blog'] = get_object_or_404(Blog, main=True)
    context['other_blog'] = Blog.objects.filter(publish=True).order_by('-pk')[:2]

    return render(request, 'index.html', context)


def contact(request):
    context = {}

    if request.method == 'POST':
        form = IndexForms(request.POST)
        if form.is_valid():
            form.save()
            context['name'] = form['name'].value()
            context['phone'] = form['phone'].value()
            context['form'] = IndexForms()
    else:
        context['form'] = IndexForms()
    return render(request, 'contacts.html', context)


def partners(request):
    context = {}

    if request.method == 'POST':
        form = PartnersForms(request.POST)
        if form.is_valid():
            form.save()
            context['name'] = form['name'].value()
            context['phone'] = form['phone'].value()
            context['email'] = form['email'].value()
            context['url'] = form['url'].value()
            context['form'] = PartnersForms()
    else:
        context['form'] = PartnersForms()
    return render(request, 'partners.html', context)


class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = {}
        return context
