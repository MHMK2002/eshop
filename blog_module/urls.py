from django.conf.urls.static import static
from django.urls import path
from django.conf import settings

from blog_module import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name='blog-list')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

