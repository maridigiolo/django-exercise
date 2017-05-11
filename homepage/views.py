# Create your views here.

from django.template.response import TemplateResponse
from django import http
from django.core.mail import send_mail


import datetime

from homepage.forms import NameForm
from homepage.forms import ContactForm

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


def hello (request):
    # print(request.GET)
    # print(request.POST)
    #
    # context = {
    #     'page_title': 'Marina Di Giolo - My profile page',
    # }

    # your_name = request.POST.get('your_name', 'Default name')
    # context = {
    #     'your_name': your_name
    # }

    form = NameForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            print(form.cleaned_data['your_name'])
            # send_email()
            return http.HttpResponseRedirect('/thanks/')

    context = {
        'form': form
    }

    return TemplateResponse(request, 'hello.html', context)


def contact_me (request):
    form = ContactForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            print(form.cleaned_data['name'])
            print(form.cleaned_data['question'])
            send_mail(
                'Subject here',
                'question',
                'from@example.com',
                ['to@example.com'],
                fail_silently=False,
            )
            return http.HttpResponseRedirect('/thanks')
        else:
            print(form.errors)
    context = {
        'form': form
    }

    return TemplateResponse(request, 'personalpage/contact_me.html', context)


def thanks (request):
    context = {
        'page_title': 'Thank you',
    }
    return TemplateResponse(request, 'personalpage/thanks.html', context)
