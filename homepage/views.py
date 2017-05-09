# Create your views here.

from django.template.response import TemplateResponse
import datetime

def homepage (request):
    context = {
        'page_title': 'HOME PAGE',
        'name': 'Marina',
        'now': datetime.datetime.now(),
        'numbers': [1, 2, 3, 4],
    }
    return TemplateResponse(request, 'homepage.html', context)

def layout (request):
    context = {
        'page_title': 'Layout - django',
        'name': 'Marina',
        'now': datetime.datetime.now(),
    }
    return TemplateResponse(request, 'pagetest/layout.html', context)

def contact (request):
    context = {
        'page_title': 'Testing',
    }
    return TemplateResponse(request, 'pagetest/contact.html', context)

def about (request):
    context = {
        'page_title': 'About page',
    }
    return TemplateResponse(request, 'pagetest/about.html', context)

def maripage (request):
    context = {
        'page_title': 'Marina Di Giolo - My profile page',
    }
    return TemplateResponse(request, 'personalpage/maripage.html', context)
