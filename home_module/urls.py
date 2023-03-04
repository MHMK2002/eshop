from django.conf.urls.static import static
from django.urls import path

from eshop import settings
from . import views

urlpatterns = [
    path('', views.index, name='home')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
