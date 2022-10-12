from django.forms import ModelForm
from .models import VacanciesForm


class VacanciesForms(ModelForm):
    class Meta:
        model = VacanciesForm
        fields = ['name', 'phone', 'email', 'url']
