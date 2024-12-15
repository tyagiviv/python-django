from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def hello(request, s):
    return HttpResponse(f'Hello, {s} world!')


def hello2(request, s0):
    s1 = request.GET.get('s1', '')
    return render(
        request, template_name='my_html.html',
        context={'adjectives': [s0, s1, 'beautiful', 'wonderful']}
    )