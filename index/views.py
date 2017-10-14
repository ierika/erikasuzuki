from django.shortcuts import render
from django.views.generic import TemplateView

from .chuck import Chuck


def index(request):
    chuck = Chuck()
    return render(request, 'index/index.html', {
        'fact': chuck.get_random_fact(),
    })
