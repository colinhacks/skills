from django.http import HttpResponse
from django.shortcuts import render
import datetime

from skills.forms import ContactForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail



def home(request):
    return HttpResponse("Check out them apples: <a href='hello' >Hello!</a>")


def test(request):
	return render(request, 'marketing.html',{'extension':'template1.html'})
	
	"""
def flyaway(request):
	return render(request, 'flyaway.html',{'extension':'template1.html'})
	"""
