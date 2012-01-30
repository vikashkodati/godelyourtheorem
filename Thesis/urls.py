from Thesis.views import start
from dajaxice.core import dajaxice_autodiscover
from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.simple import direct_to_template

dajaxice_autodiscover()

# Uncomment the next two lines to enable the admin:
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Thesis.views.home', name='home'),
    # url(r'^Thesis/', include('Thesis.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

    url(r'^$', start), 
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/profile', direct_to_template,  {'template': 'home.html'},  name="profile"),  
    (r'^accounts/', include('registration.backends.default.urls')), 
    (r'^%s/' % settings.DAJAXICE_MEDIA_PREFIX, include('dajaxice.urls')),

)

urlpatterns += staticfiles_urlpatterns()
