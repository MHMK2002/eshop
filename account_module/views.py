from django.shortcuts import render, redirect
from django.views.generic import View

from account_module.forms import RegisterForm
from account_module.models import User


# Create your views here.


class RegisterUser(View):
    def get(self, request):
        register_form = RegisterForm()
        context = {
            'register_form': register_form
        }
        template = 'account_module/register-page.html'
        return render(request, template, context)

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            user = User(username=username, email=email, password=password)
            user.save()
            return redirect('home')

        context = {
            'register_form': register_form
        }

        return render(request, 'account_module/register-page.html', context)
