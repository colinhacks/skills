from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
import datetime
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib.auth.middleware import RemoteUserMiddleware
from django.contrib.auth.backends import RemoteUserBackend
from django.contrib import auth
from django.contrib.auth import REDIRECT_FIELD_NAME, authenticate
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
import settings
from django.contrib.auth.models import User
from userapp.forms import FullUserCreationForm
from skillapp.models import Skill
from messageapp.models import Message, MessageThread
template = 'template1.html'

def home(request):
    return HttpResponse("Check out them apples: <a href='hello' >Hello!</a>")

def login(request, *args, **kwargs):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/profile/'+str(request.user.id))
    if request.method == 'POST':
        data = request.POST
        username = User.objects.get(email=request.POST['email']).username
        password=request.POST['password']
        user = auth.authenticate(username=username, password=password)
        auth.login(request, user)
        return HttpResponseRedirect('/profile/'+str(request.user.id))
    else:
        return render(request, kwargs['template'],{'extension':kwargs['extension']})

def create(request, *args, **kwargs):
    if request.method == 'POST':
        import re
        data = request.POST
        files = request.FILES
        now = datetime.datetime.now()
        username = re.sub('[@.!#$%^&*()\-+=~`?/|\\:;\"\'}{\][.,<>]', '', request.POST['email'])
        data['username'] = username
        data['classYear'] = request.POST['classYear']
        data['date_joined'] = now
        data['last_login'] = now
        data['password'] = data['password1']
        user = FullUserCreationForm(data, files)
        postdatakeys = data.keys()
        postdatavals = data.values()

        if user.is_valid():
            user.save()
            user = authenticate(username=username, password=request.POST['password1'])
            auth.login(request, user)
            return HttpResponseRedirect('/addskills/')
        else:
            return render(request, 'create.html',{'extension':'template1.html','data':user.cleaned_data,'form':user})
    else:
        user = FullUserCreationForm(auto_id=False)
        return render(request, kwargs['template'],{'form':user,'extension':template})

def test(request):
    return render(request, 'marketing.html',{'extension':template})

@login_required
def enterskills(request):
    if request.method == "POST":
        import re
        enteredskills = request.POST["actual"].split("&&")
        prof=request.user.get_profile()
        for skill in enteredskills:
            skill= re.sub(r'\!\=\*\$&<[^>]*?>', '', skill.strip().strip("*=\\><"))
            uglyname=skill.replace(" ","_").lower()
            if skill:
                existing = Skill.objects.filter(uglyname=uglyname,)
                if existing:
                    prof.skills.add(existing[0])
                    prof.save()
                else:
                    new = Skill(name=skill, uglyname=uglyname)
                    new.save()
                    prof.skills.add(new)
                    prof.save()
        return HttpResponseRedirect("/profile/"+str(request.user.id))

    skills = request.user.get_profile().skills.all()
    allskills = Skill.objects.all()
    if skills:
        return render(request,'enterskills.html',{'skills':skills,'allskills':allskills,'extension':template})
    else: 
        return render(request,'enterskills.html',{'allskills':allskills,'extension':template})


def profile(request, id):
    if int(id) == request.user.id:
        return redirect('/you/')
    else:
        user = User.objects.get(pk=int(id))        
        skills = user.get_profile().skills.order_by('name')
        bio = user.get_profile().additional
        allskills = Skill.objects.all()
        profile = user.get_profile()
        try:
            picture = profile.picture.url
        except:
            picture = settings.MEDIA_ROOT+"/default.jpg"
        return render(request, 'profile.html',{'extension':template,'user':user,'profile':profile, 'skills':skills,'bio':bio,'allskills':allskills,'picture':picture})

def you(request):
    user = request.user      
    skills = user.get_profile().skills.all()
    allskills = Skill.objects.all()
    try:
        profile = user.get_profile()
    except:
        profile = NewUserProfile()
        profile.user - request.user
    try:
        picture = profile.picture.url
    except:
        picture = settings.MEDIA_ROOT+"/default.jpg"
    return render(request, 'profile.html',{'picture':picture,'extension':template,'user':user,'profile':profile, 'skills':skills,'allskills':allskills})

def skill(request, skillname):
    skill = get_object_or_404(Skill, uglyname=skillname)
    name=skill.name
    uglyname = skill.uglyname
    return render(request, 'skill.html',{'extension':template,'name':name,'uglyname':uglyname})
    

def again(request):
    return render(request, 'marketing.html',{'extension':template})
	
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")

def testing(request):
    return render(request, 'marketing.html',{'extension':template})
    
def loginRedirect(request):
    return HttpResponseRedirect("")
"""
def flyaway(request):
	return render(request, 'flyaway.html',{'extension':template})
"""

def send_message(request):
    try:
        if request.METHOD=='POST':
            user_pks = request.POST.getlist(['users[]'])
            text = request.POST['message']
            users = [User.objects.get(pk=pk) for pk in user_pks]
            userstring = '&'.join(sorted(user_pks))
            message = Message(text=text.strip())
            
            threads = MessageThread.objects.filter(userstring=userstring)
            if MessageThread.objects.filter(userstring=userstring):
                thread = threads[0]
            else:
                thread = MessageThread()
                for pk in user_pks:
                    thread.users.add(User.objects.get(pk=pk))
            thread.save()

            message.thread=thread
            message.save()
            return "Message Sent"
        else:
            pass
    except:
        return "Server Error.  Please try again."

def remove_skill(request):
    if request.is_ajax():
        try:
            skill = Skill.objects.get(name=request.POST['skill'])
            request.user.get_profile().skills.remove(skill)
            return HttpResponse("Yay!")
        except:
            return HttpResponse('Server error.  Youism not deleted.') # incorrect post
    else:
        return HttpResponse("Not ajax.")

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