from django.urls import path
from .views import *

urlpatterns = [
    path('services/', ServicesView.as_view(), name='services'),
    path('architecture/', ArhView.as_view(), name='architecture'),
    path('residential/', JilView.as_view(), name='residential'),
    path('commercial/', KomView.as_view(), name='commercial'),
    path('project/', ProjectView.as_view(), name='project'),
]
