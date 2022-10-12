from django.http import JsonResponse
from .forms import *
from ..vacancies.forms import VacanciesForms


def is_ajax(request):
    return request.headers.get('x-requested-with') == 'XMLHttpRequest'


def contact_form(request):
    if request.method == "POST" and is_ajax(request):
        form = IndexForms(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"ok": True}, status=200)
        else:
            return JsonResponse({"ok": False}, status=400)


def partners_form(request):
    if request.method == "POST" and is_ajax(request):
        form = PartnersForms(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"ok": True}, status=200)
        else:
            return JsonResponse({"ok": False}, status=400)


def vacancies_form(request):
    if request.method == "POST" and is_ajax(request):
        form = VacanciesForms(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"ok": True}, status=200)
        else:
            return JsonResponse({"ok": False}, status=400)
