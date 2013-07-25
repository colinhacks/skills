from django.conf.urls import patterns, include, url



# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('skills.views',
    
    url(r'^$', 'home'),
    url(r'^again/$', 'again'),

    # url(r'^initial/', include('initial.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
     #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     #url(r'^admin/', include(admin.site.urls)),
     url(r'^test/$', 'test'), 
     url(r'^form/$', 'form1')



)
