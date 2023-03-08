from django.core.paginator import Paginator
from django.views.generic import ListView

from blog_module.models import Blog


# Create your views here.

class BlogListView(ListView):
    model = Blog
    paginate_by = 1
    template_name = 'blog_module/blog-list.html'

    def get_queryset(self, *args, **kwargs):
        qs = super(BlogListView, self).get_queryset()
        qs = qs.order_by('-date_created')
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        blogs = Blog.objects.filter(is_active=True).order_by('-date_created')
        paginator = Paginator(blogs, 4)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        context['request'] = self.request
        return context
