import logging

from django import forms
from django.core.exceptions import ValidationError
from .models import User
import re


class RegisterForm(forms.Form):
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={
        'placeholder': 'رمزعبور'
    }))
    confirm_password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={
        'placeholder': 'تکرار رمز عبور'
    }))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': 'نام کاربری',
    }))
    email = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': 'ایمیل'
    }))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        exits: bool = User.objects.all().filter(username__exact=username)
        if exits:
            raise ValidationError(message='یک کاربر با این نام کاربری وجود دارد.\n'
                                          'لطفا نام کاربری دیگری انتخاب کنید.')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        exits: bool = User.objects.all().filter(email__exact=email)
        if exits:
            raise ValidationError(message='این ایمیل قبلا استفاده شده است.')
        return email

    def clean_confirm_password(self):
        confirm_password = self.cleaned_data.get('confirm_password')
        password = self.cleaned_data.get('password')
        if password != confirm_password:
            raise ValidationError(message='رمز عبور با تکرار رمز عبور مغایرت دارد.')

        password_pattern = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-_]).{8,}$"
        if re.match(password_pattern, password) is None:
            raise ValidationError(message='پسورد معتبر نمی باشد.')
        return confirm_password


class LoginForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'پسورد'
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'نام کاربری'
    }))


