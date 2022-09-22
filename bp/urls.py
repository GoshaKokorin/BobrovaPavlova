from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from apps.index.urls import urlpatterns as index_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
]
urlpatterns += index_urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
