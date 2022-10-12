from django.urls import path
from .views import *
from .backend import contact_form

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contact, name='contacts'),
    path('partners/', partners, name='partners'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact-form/', contact_form, name='contact_form')
]
