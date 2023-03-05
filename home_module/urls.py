from django.conf.urls.static import static
from django.urls import path

from eshop import settings
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about-us', views.AboutUsView.as_view(), name='about_us')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
