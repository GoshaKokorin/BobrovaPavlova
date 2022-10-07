from django.urls import path
from .views import *

urlpatterns = [
    path('services/', ServicesView.as_view(), name='services'),
    path('services/<str:slug_service>/', single_services, name='single_services'),
    path('services/<str:slug_service>/<str:slug_project>/', project, name='services_project'),
]
