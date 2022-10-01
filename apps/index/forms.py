from django.forms import ModelForm
from .models import IndexForm, PartnersForm


class IndexForms(ModelForm):
    class Meta:
        model = IndexForm
        fields = ['name', 'phone']


class PartnersForms(ModelForm):
    class Meta:
        model = PartnersForm
        fields = ['name', 'phone', 'email', 'url']
