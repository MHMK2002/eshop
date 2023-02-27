from django import forms

from contact_module.models import ContactUs


class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'نام و نام خانوادگی'
    }))
    email = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'ایمیل'
    }))
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'موضوع'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'متن پیام',
        'id': 'message'
    }))


class ConatctUsModelForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name', 'title', 'message', 'email']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام و نام خانوادگی'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ایمیل'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'موضوع'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'متن پیام',
                'id': 'message'
            })
        }
