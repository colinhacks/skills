
from django.http import HttpResponse
from django.shortcuts import render
import datetime

from skills.forms import ContactForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib.auth.middleware import RemoteUserMiddleware
from django.contrib.auth.backends import RemoteUserBackend
from django.contrib.auth.views import login
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
import settings


def home(request):
    return HttpResponse("Check out them apples: <a href='hello' >Hello!</a>")


def test(request):
    return render(request, 'marketing.html',{'extension':'template1.html'})

def again(request):
    return render(request, 'marketing.html',{'extension':'template1.html'})
	
def testing(request):
    return render(request, 'test2.html',{'extension':''})
    

"""
def flyaway(request):
	return render(request, 'flyaway.html',{'extension':'template1.html'})
"""
def create(request):
    pass


def scripts_login(request, **kwargs):
    host = request.META['HTTP_HOST'].split(':')[0]
    if host == 'localhost':
        return login(request, **kwargs)
    elif request.META['SERVER_PORT'] == '444':
        if request.user.is_authenticated():
            # They're already authenticated --- go ahead and redirect
            if 'in' in kwargs:
                redirect_field_name = kwargs['in']
            else:
                from django.contrib.auth import REDIRECT_FIELD_NAME
                redirect_field_name = REDIRECT_FIELD_NAME
            redirect_to = request.REQUEST.get(redirect_field_name, '')
            if not redirect_to or '//' in redirect_to or ' ' in redirect_to:
                redirect_to = settings.LOGIN_REDIRECT_URL
            return HttpResponseRedirect(redirect_to)
        else:
            return login(request, **kwargs)
    else:
        # Move to port 444
        redirect_to = "https://%s:444%s" % (host, request.META['REQUEST_URI'], )
        return HttpResponseRedirect(redirect_to)