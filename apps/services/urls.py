from django.urls import path
from .views import *

urlpatterns = [
    path('services/', ServicesView.as_view(), name='services'),
    path('architecture/', ArhView.as_view(), name='architecture'),
    path('residential/', JilView.as_view(), name='residential'),
    path('commercial/', KomView.as_view(), name='commercial'),
    path('east_legend/', Project1View.as_view(), name='east_legend'),
    path('itmo/', Project2View.as_view(), name='itmo'),
    path('market/', Project3View.as_view(), name='market'),
    path('mogaisky/', Project4View.as_view(), name='mogaisky'),
    path('sosnovka/', Project5View.as_view(), name='sosnovka'),
    path('strelna/', Project6View.as_view(), name='strelna'),
    path('project/', Project7View.as_view(), name='project'),
]
