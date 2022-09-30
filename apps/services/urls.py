from django.urls import path
from .views import *

urlpatterns = [
    path('services/', ServicesView.as_view(), name='services'),
]
