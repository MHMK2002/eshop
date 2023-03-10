from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from blog_module.models import Blog, BlogCategory, BlogComment


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
        blog = Blog.objects.filter(slug__iexact=slug).first()
        comments = blog.blogcomment_set.filter(replay=None).order_by('-date_created')
        tags = blog.tags.all()[:3]
        count = blog.blogcomment_set.count()
        context = {
            'blog': blog,
            'comments': comments,
            'tags': tags,
            'count': count,
        }
        return render(request, 'blog_module/blog_detail.html', context)

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


def comment_component(request: HttpRequest, comment_id: int):
    comment = BlogComment.objects.filter(id=comment_id).first()
    sub_comments = comment.blogcomment_set.order_by('-date_created')
    context = {
        'comment': comment,
        'sub_comments': sub_comments
    }
    template = 'blog_module/comment-component.html'
    return render(request, template, context)


def add_comment(request):
    if request.user.is_authenticated:
        auther_id = request.user.id
        comment_text = request.GET['comment_text']
        blog_id = request.GET['blog_id']
        replay_id = None if request.GET['replay_id'] == '' else request.GET['replay_id']
        comment = BlogComment(blog_id=blog_id,
                              auther_id=auther_id,
                              text=comment_text,
                              replay_id=replay_id)
        comment.save()

    return HttpResponse('hello')
