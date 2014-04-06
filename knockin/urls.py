from django.conf.urls import patterns, include, url
import padkey
from padkey import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'padkey.views.passcode', name='passcode'),
    url(r'^admin/$', 'padkey.views.generate_passcode', name='admin'),
    url(r'^login/$', 'padkey.views.login_view', name='login'),
    url(r'^logout/$', 'padkey.views.logout_view', name='logout'),
    url(r'^sms/$', 'sms.views.receive_message', name='sms_receive'),
    # Examples:
    # url(r'^$', 'knockin.views.home', name='home'),
    # url(r'^knockin/', include('knockin.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
