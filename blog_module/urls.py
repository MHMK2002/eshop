from django.conf.urls.static import static
from django.urls import path
from django.conf import settings

from blog_module import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name='blog-list'),
    path('add-comment', views.add_comment, name='add_comment'),
    path('cat/<str:title_url>', views.BlogByCategoryListView.as_view(), name='blog_by_category'),
    path('<int:pk>/<slug:slug>', views.BlogDetailView.as_view(), name='blog_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

