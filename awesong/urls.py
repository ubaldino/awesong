from django.conf.urls import patterns, include, url
from django.contrib import admin
from core.views import inicio
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', inicio),
     #url(r'^awesong/', include('awesong.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
