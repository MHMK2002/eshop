import re
import string

from django.template.defaultfilters import slugify, random


def get_unique_slug(id, title, obj):
    slug = slugify(title.replace('ı', 'i'))
    unique_slug = slug
    counter = 1
    while obj.filter(slug=unique_slug).exists():
        if obj.filter(slug=unique_slug).values('id')[0]['id'] == id:
            break
        unique_slug = '{}-{}'.format(slug, counter)
        counter += 1
    return unique_slug
