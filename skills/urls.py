from django.conf.urls import patterns, include, url
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import login, logout


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('skills.views',
    
    url(r'^$', login, {'template_name':'login.html','extra_context':{'extension':'template1.html'}}),
    url(r'^create/$', 'login',{'in':'create'}),
    url(r'^testing/$', 'testing'),

    # url(r'^initial/', include('initial.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
     #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     #url(r'^admin/', include(admin.site.urls)),
     url(r'^test/$', 'test'), 
     url(r'^form/$', 'form1')



)
