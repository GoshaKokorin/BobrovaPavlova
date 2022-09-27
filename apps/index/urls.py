from django.urls import path

from apps.index.views import IndexView, ContactsView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contacts/', ContactsView.as_view(), name='index'),
]