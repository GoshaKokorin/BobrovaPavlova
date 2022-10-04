from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView
from apps.index.forms import IndexForms, PartnersForms


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
            # return render(request, 'about.html', context)
        else:
            errors = form.errors.as_json()
            # return JsonResponse({"errors": errors}, status=400)
    else:
        context['form'] = IndexForms()
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
