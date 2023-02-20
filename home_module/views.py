from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.

def sidebar_partial(request):
    return render(request=request, template_name='home_module/shared/sidebar.html')


def header_partial(request):
    return render(request=request, template_name='home_module/shared/header.html')


def footer_partial(request):
    return render(request=request, template_name='home_module/shared/footer.html')


def reverse_home(request):
    return HttpResponseRedirect(reverse('home'))


def home(request):
    return render(request=request, template_name='home_module/home.html')
