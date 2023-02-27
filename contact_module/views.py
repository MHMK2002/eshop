from django.http import HttpResponseRedirect
from django.shortcuts import render

from contact_module.fomrs import ContactUsForm
from contact_module.models import ContactUs


# Create your views here.


def contact_us(request):
    contact_form = ContactUsForm(request.POST or None)
    if contact_form.is_valid():
        contact_module = ContactUs(name=request.POST['name'], email=request.POST['email'], title=request.POST['title'],
                                   message=request.POST['message'])
        contact_module.save()
        return HttpResponseRedirect('home')

    return render(request, 'contact_module/contact-us.html', {
        'contact_form': contact_form
    })
