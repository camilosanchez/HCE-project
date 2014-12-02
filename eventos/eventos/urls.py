#encoding: utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.site.site_header = 'Sistema de administración de eventos'

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'eventos.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include('apps.events.urls', namespace="events_app")),
    url(r'^admin/', include(admin.site.urls)),
)