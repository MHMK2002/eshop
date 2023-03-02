from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.html import strip_tags


def send_email(subject, to, template, context):
    try:
        from_email = settings.EMAIL_HOST_USER
        html_message = render_to_string(template, context)
        plain_message = strip_tags(html_message)
        send_mail(subject=subject, from_email=from_email, message=plain_message, html_message=html_message,
                  recipient_list=[to])
    except Exception as ex:
        print(ex)
