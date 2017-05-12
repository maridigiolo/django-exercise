from django.template.response import TemplateResponse
from django.shortcuts import get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect

from polls.models import Poll, Choice, Category

def index(request):
    polls = Poll.objects.all()

    category = request.GET.get('category', '')
    if category:
        polls = polls.filter(categories__slug=category)

    return TemplateResponse(request, 'polls.html', {'polls': polls})

def answer(request, pollslug):
    choices = Choice.objects.filter(question__slug=pollslug)
    return TemplateResponse(request, 'answer.html', {'choices': choices})

def vote (request, pollslug, choice_id):
    # lookup the choice

    # add a vote
    # save
    return HttpResponseRedirect('../../')
