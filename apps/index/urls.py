from django.urls import path

from apps.index.views import *

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('blog/blog_single/', BlogSingleView.as_view(), name='blog_single'),
    path('partners/', PartnersView.as_view(), name='partners'),
    path('about/', AboutView.as_view(), name='about'),
    path('architecture/', ArhView.as_view(), name='architecture'),
    path('residential/', JilView.as_view(), name='residential'),
    path('commercial/', KomView.as_view(), name='commercial'),
    path('project/', KomView.as_view(), name='project'),
]
