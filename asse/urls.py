from django.conf.urls import patterns, url

from asse import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
	url(r'^result/$', views.result, name='result')
)