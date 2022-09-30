from django.forms import ModelForm
from .models import IndexForm


class IndexForms(ModelForm):
    class Meta:
        model = IndexForm
        fields = ['name', 'phone']
