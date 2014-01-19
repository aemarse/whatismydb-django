from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^whatismydb/', include('whatismydb.urls', namespace="whatismydb")),
    url(r'^admin/', include(admin.site.urls)),
)