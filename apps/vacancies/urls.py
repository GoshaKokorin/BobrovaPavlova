from django.urls import path
from .views import *

urlpatterns = [
    path('vacancies/', VacanciesView.as_view(), name='vacancies'),
]
