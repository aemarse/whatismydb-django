from django.conf.urls import patterns, url

from whatismydb import views

urlpatterns = patterns('',
	url(r'^$', views.home, name='home'),
	url(r'^poster/$', views.poster, name='poster'),
)