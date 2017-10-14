from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


class IndexView(View):
    def get(self, request):
        return HttpResponse('''
            <h1>Don\'t know what to do with this site yet.</h1>
        ''')
