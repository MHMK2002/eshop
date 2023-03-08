from django.conf.urls.static import static
from django.urls import path
from django.conf import settings

from blog_module import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name='blog-list'),
    path('cat/<str:title_url>', views.BlogByCategoryListView.as_view(), name='blog_by_category')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

