from django.urls import path
from apps.blog.views import *

urlpatterns = [
    path('blog/', BlogView.as_view(), name='blog'),
    path('blog/blog_single/', BlogSingleView.as_view(), name='blog_single'),
]
