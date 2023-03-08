from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from blog_module.models import Blog, BlogCategory


# Create your views here.

class BlogListView(ListView):
    model = Blog
    paginate_by = 4
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
        context['title'] = ''
        return context


class BlogByCategoryListView(ListView):
    model = Blog
    paginate_by = 4
    template_name = 'blog_module/blog-list.html'

    def get_queryset(self, *args, **kwargs):
        qs = super(BlogByCategoryListView, self).get_queryset().filter(
            blog_categories__title_url__iexact=kwargs.get('title_url'))
        qs = qs.order_by('-date_created')
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        category = BlogCategory.objects.filter(title_url__iexact=kwargs.get('title_url')).first()
        blogs = category.blog_set.all()
        paginator = Paginator(blogs, 4)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        context['request'] = self.request
        context['title'] = category.title
        return context


class BlogDetailView(View):
    def get(self, request, slug):
        template = 'blog_module/blog_detail.html'
        blog = Blog.objects.filter(slug__iexact=slug).first()
        context = {
            'blog': blog
        }
        return render(request, template, context)

    def post(self, request, slug):
        pass


def category_sidebar_component(request, title_url):
    category = BlogCategory.objects.filter(title_url__exact=title_url).first()
    context = {
        'category': category
    }
    return render(request, 'blog_module/category_sidebar_component.html', context)


def category_sidebar(request):
    main_categories = BlogCategory.objects.all().filter(parent=None)
    context = {
        'main_categories': main_categories
    }
    return render(request, 'blog_module/category_sidebar.html', context)
