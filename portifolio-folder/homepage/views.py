# Create your views here.

from django.template.response import TemplateResponse

def homepage (request):
  return TemplateResponse(request, 'homepage.html', {})
