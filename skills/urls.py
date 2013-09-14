from django.conf.urls import patterns, include, url
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import login, logout
from skills import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('skills.views',
    
    #url(r'^$', 'login', {'template_name':'login.html','extra_context':{'extension':'template1.html'}}),
    url(r'^$', 'login', {'template':'login.html','extension':'template1.html'}),
    url(r'^create/$', 'create',{'template':'create.html','in':'create'}),
    url(r'^testing/$', 'testing'),
    url(r'^addskills/$', 'enterskills'),
    url(r'^you/$', 'you'),
    url(r'^profile/(?P<id>[0-9]+)$', 'profile'),
    url(r'^skill/(?P<skillname>[a-zA-Z0-9_]+)$', 'skill'),
    url(r'^logout/$', 'logout'),
    url(r'^messages/admin_send/$', 'send_message'),
    url(r'^skills/removeskill/$', 'remove_skill'),


    # url(r'^initial/', include('initial.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
     #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
     url(r'^test/$', 'test'), 
     #url(r'^form/$', 'form1')
)

if settings.SERVE_MEDIA:
    urlpatterns += patterns("",
        (r'^skills/static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.STATIC_ROOT, 'show_indexes': True }),
        (r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, }),
        )
