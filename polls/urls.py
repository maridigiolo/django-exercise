from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(\S+)/answer/$', views.answer, name='answer'),
    url(r'^(\S+)/vote/(\d+)/$', views.vote, name='vote'),
]
