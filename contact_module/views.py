from django.http import HttpResponseRedirect
from django.shortcuts import render

from contact_module.models import ContactUs


# Create your views here.


def contact_us(request):
    return render(request, 'contact_module/contact-us.html')


def submit_message(request):
    title = request.POST['title']
    message = request.POST['message']
    email = request.POST['email']
    name = request.POST['name']
    message = ContactUs(title=title, message=message, email=email, name=name)
    message.save()
    return HttpResponseRedirect('home')
