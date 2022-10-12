from django.http import JsonResponse
from .forms import *


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
