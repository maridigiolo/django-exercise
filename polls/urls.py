from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # url(r'^(\S+)/answer/$', views.answer, name='answer'),
    # url(r'^(\S+)/vote/(\d+)/$', views.vote, name='vote'),
]
