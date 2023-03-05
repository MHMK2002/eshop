from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.views import View

from home_module.models import Slider, FooterLinkBox
from site_module.models import SiteSettings


class HomeView(View):
    def get(self, request: HttpRequest):
        sliders: Slider = Slider.objects.filter(is_active=True)
        settings: SiteSettings = SiteSettings.objects.filter(mail_setting=True).first()
        context = {
            'sliders': sliders,
            'settings': settings
        }
        return render(request, 'home_module/index.html', context)

    def post(self, request):
        pass


class AboutUsView(View):
    def get(self, request: HttpRequest):
        return render(request, 'home_module/about-us.html', {
            'settings': SiteSettings.objects.all().first()
        })


def header_component(request):
    context = {
        'settings': SiteSettings.objects.all().first()
    }
    return render(request, 'shared/header.html', context)


def footer_component(request):
    link_boxes = FooterLinkBox.objects.filter(is_active=True)
    context = {
        'link_boxes': link_boxes,
        'settings': SiteSettings.objects.all().first()
    }
    return render(request, 'shared/footer.html', context)
