from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from practice2.models import UserProfile
from skills.living import livingGroups,majorChoices,yearChoices


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
    	email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).count():
            raise forms.ValidationError(u'Email addresses must be unique.')
        return email

    def clean_first_name(self):
        first = self.cleaned_data.get('first_name')
        if first=='' or first=="First":
            raise forms.ValidationError(u'First name is required.')
        return first 

    def clean_last_name(self):
        last = self.cleaned_data.get('last_name')
        if last=='' or last=="Last":
            raise forms.ValidationError(u'Last name is required.')
        return last    

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
        
        user = super(FullUserCreationForm, self).save(commit=False) 
        user.save()

        try:
            profile = user.get_profile()
        except:
            profile = UserProfile(user=user)

        profile.classYear = self.cleaned_data['classYear']
        profile.major = self.cleaned_data['major']
        profile.livingGroup = self.cleaned_data['livingGroup']
        if self.cleaned_data['picture']:
        	profile.picture = self.cleaned_data['picture']
        if self.cleaned_data['additional']:
        	profile.additional = self.cleaned_data['additional']
        profile.save()
        return user

class ContactForm(forms.Form):
    subject = forms.CharField()
    email = forms.EmailField(required=False)
    message = forms.CharField(widget=forms.Textarea)
    