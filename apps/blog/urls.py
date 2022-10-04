from django.urls import path
from apps.blog.views import *

urlpatterns = [
    path('blog/', BlogView.as_view(), name='blog'),
    path('blog/<str:slug_blog>/', blog_single, name='blog_single'),
]
