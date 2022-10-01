from django.urls import path
from apps.index.views import *

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contact, name='contacts'),
    path('partners/', partners, name='partners'),
]
