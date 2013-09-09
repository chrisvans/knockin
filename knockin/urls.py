from django.conf.urls import patterns, include, url
import padkey
from padkey import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'padkey.views.passcode', name='passcode'),
    # Examples:
    # url(r'^$', 'knockin.views.home', name='home'),
    # url(r'^knockin/', include('knockin.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
