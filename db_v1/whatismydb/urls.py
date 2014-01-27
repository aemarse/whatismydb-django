from django.conf.urls import patterns, url

from whatismydb import views

urlpatterns = patterns('',
	url(r'^$', views.home, name='home'), # Main url
	url(r'^poster/$', views.poster, name='poster'), # Poster url
)