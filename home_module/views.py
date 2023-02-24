from django.shortcuts import render
from django.http import HttpResponseRedirect


def index(request):
    return render(request, 'home_module/index.html')


def home(request):
    return HttpResponseRedirect(redirect_to='home')


def header_component(request):
    return render(request, 'shared/header.html')


def footer_component(request):
    return render(request, 'shared/footer.html')

