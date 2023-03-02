from django.contrib.auth import login
from django.http import HttpRequest, Http404
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
            user.is_active = False
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

    def post(self, request):
        login_form = LoginForm(request.POST)
        context = {
            'login_form': login_form
        }
        username = request.POST['username']
        password = request.POST['password']
        user: User = User.objects.all().filter(username__exact=username).first()
        if user is None:
            login_form.add_error('username', 'نام کاربری و یا کلمه عبور اشتباه است.')
            return render(request, 'account_module/login-register.html', context)
        if not user.check_password(password):
            login_form.add_error('username', 'نام کاربری و یا کلمه عبور اشتباه است.')
            return render(request, 'account_module/login-register.html', context)
        if not user.is_active:
            login_form.add_error('username', 'اکانت شما فعال نشده است.')
            return render(request, 'account_module/login-register.html', context)
        login(request, user)
        return redirect('home')


class ActivationUser(View):
    def get(self, request, email_activation_code):
        user: User = User.objects.all().filter(email_activation_code__exact=email_activation_code).first()
        if user is None:
            raise Http404
        if user.is_active:
            # todo: show error message
            pass
        else:
            user.is_active = True
            user.email_activation_code = get_random_string(72)
            return redirect('login-page')
