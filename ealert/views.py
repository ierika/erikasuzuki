from django.shortcuts import render
from django.template.loader import get_template
from django.http import Http404

from unipath import Path


def email(request, slug):
    template_name = 'ealert/{}'.format(slug)
    try:
        get_template(template_name)
    except:
        raise Http404('Email does not exist')
    return render(request, template_name)
