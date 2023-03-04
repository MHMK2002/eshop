from django.http import HttpResponseRedirect
from django.shortcuts import render

from contact_module.fomrs import ContactUsForm, ConatctUsModelForm
from django.views.generic import FormView

from site_module.models import SiteSettings


# Create your views here.


class ContactUsView(FormView):
    template_name = 'contact_module/contact-us.html'
    form_class = ConatctUsModelForm
    success_url = 'home'

    def valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['settings'] = SiteSettings.objects.all().first()
        return context
