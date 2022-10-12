from django.urls import path
from .views import *
from .backend import *

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contact, name='contacts'),
    path('partners/', partners, name='partners'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact-form/', contact_form, name='contact_form'),
    path('partners-form/', partners_form, name='partners_form'),
    path('vacancies-form/', vacancies_form, name='vacancies_form')
]
