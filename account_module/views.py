from django.shortcuts import render, redirect
from django.views.generic import View
from django.utils.crypto import get_random_string
from account_module.forms import RegisterForm, LoginForm
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
            user = User(username=username, email=email, email_activation_code=get_random_string(72))
            user.set_password(password)
            user.save()
            # TODO: send activation code
            return redirect('login-page')

        context = {
            'register_form': register_form
        }

        return render(request, 'account_module/register-page.html', context)


class LoginUser(View):
    def get(self, request):
        login_form = LoginForm()
        context = {
            'login_form': login_form
        }
        return render(request, 'account_module/login-register.html', context)

    def post(self):
        pass
