from django.http import HttpRequest
from django.shortcuts import render
from django.views import View

from site_module.models import SiteSettings


# Create your views here.

class AboutUsView(View):
    def get(self, request: HttpRequest):
        return render(request, 'about_us_module/about-us.html', {
            'settings': SiteSettings.objects.all().first()
        })
