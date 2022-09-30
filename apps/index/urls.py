from django.urls import path

from apps.index.views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('partners/', PartnersView.as_view(), name='partners'),
    path('about/', AboutView.as_view(), name='about'),
]
