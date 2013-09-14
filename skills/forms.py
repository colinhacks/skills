from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from skills.models import UserProfile
from skills.living import livingGroups,majorChoices,yearChoices
import datetime

class FullUserCreationForm(UserCreationForm):
    error_css_class = "error"

    classYear = forms.ChoiceField(choices=yearChoices)
    major = forms.ChoiceField(choices=majorChoices)
    livingGroup = forms.ChoiceField(choices=livingGroups)
    picture = forms.ImageField(required=False)
    additional = forms.CharField(widget=forms.Textarea,required=False)
    class Meta:
    	model = User
    
    def clean_email(self):
        if email and User.objects.filter(email=email).exclude(username=username).count():
            raise forms.ValidationError(u'Email addresses must be uniquer.')
        return email

    def clean_major(self):
        if self.cleaned_data['major']=='Major':
            raise forms.ValidationError(u'Please select a major.')
        return self.cleaned_data['major']

    def clean_livingGroup(self):
        if self.cleaned_data['livingGroup']=='Residence':
            raise forms.ValidationError(u'Please select a residence.')
        self.cleaned_data['livingGroup']

    def clean_classYear(self):
        if self.cleaned_data['classYear']=='Class Year':
            raise forms.ValidationError(u'Please select a class year.')
        self.cleaned_data['classYear']

    def save(self, commit=False):
        username = str(int(User.objects.order_by('-date_joined')[0].username)+1)
        password1=self.cleaned_data['password1']
        password2=self.cleaned_data['password2']
        password=self.cleaned_data['password2']
        email=self.cleaned_data['email']
        first_name=self.cleaned_data['first_name']
        last_name=self.cleaned_data['last_name']
        now=datetime.datetime.now()
        
        user_data={'username':username,'password1':password1,'password2':password2,'email':email,'first_name':first_name,'last_name':last_name,'date_joined':now,'last_login':now}
        user = UserCreationForm(user_data)
        if user.is_valid():
            user.password=user.password2
            user.save()

        try:
            profile = user.get_profile()
        except:
            profile = UserProfile(user=self.cleaned_data['username'])

        profile.classYear = self.cleaned_data['classYear']
        profile.major = self.cleaned_data['major']
        profile.livingGroup = self.cleaned_data['livingGroup']
        if self.cleaned_data['picture']:
        	profile.picture = self.cleaned_data['picture']
        if self.cleaned_data['additional']
        	profile.additional; = self.cleaned_data['additional']
        profile.save()
        return user

class ContactForm(forms.Form):
    subject = forms.CharField()
    email = forms.EmailField(required=False)
    message = forms.CharField(widget=forms.Textarea)
    