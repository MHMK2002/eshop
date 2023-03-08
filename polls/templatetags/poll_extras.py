from django import template
from jalali_date import date2jalali

register = template.Library()


@register.filter(name='to_jalali')
def to_jalali(value):
    return date2jalali(value)