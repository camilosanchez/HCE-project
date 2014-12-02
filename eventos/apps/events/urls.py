from django.conf.urls import patterns, url

from .views import RegisterStepsWizard
from .views import FORMS

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'eventos.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^steps/$', RegisterStepsWizard.as_view(FORMS), name='home'),

)