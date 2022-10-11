from django.urls import path
from apps.index.views import *

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contact, name='contacts'),
    path('partners/', partners, name='partners'),
    path('about/', AboutView.as_view(), name='about'),
    path('error/', ErrorView.as_view(), name='error'),
]
