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
        username = self.cleaned_data['username']
        temp_user = User.objects.all().filter(username=username)
        if len(temp_user) == 0:
            return username
        raise ValidationError(message='یک کاربر با این نام کاربری وجود دارد.\n'
                                      'لطفا نام کاربری دیگری انتخاب کنید.')

    def clean_confirm_password(self):
        confirm_password = self.cleaned_data.get('confirm_password')
        password = self.cleaned_data.get('password')
        if password != confirm_password:
            raise ValidationError(message='رمز عبور با تکرار رمز عبور مغایرت دارد.')
        else:
            return confirm_password
