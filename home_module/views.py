from django.shortcuts import render
from django.http import HttpResponseRedirect

from site_module.models import SiteSettings


def index(request):
    return render(request, 'home_module/index.html')


def header_component(request):
    context = {
        'settings': SiteSettings.objects.all().first()
    }
    return render(request, 'shared/header.html', context)


def footer_component(request):
    context = {
        'settings': SiteSettings.objects.all().first()
    }
    return render(request, 'shared/footer.html', context)
