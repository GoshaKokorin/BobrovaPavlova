from django.urls import path
from apps.index.views import *

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('partners/', PartnersView.as_view(), name='partners'),
]
