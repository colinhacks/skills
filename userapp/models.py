from django.db import models
from skills.living import livingGroups, yearChoices, majorChoices
# Create your models here.
import datetime
from django.db.models.signals import post_save
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

import datetime
from django.db.models import Count
from django.contrib.auth.models import User

from skillapp.models import Skill

# Create your models here.

# DEFINE SKILL
    
def content_file_name(instance, filename):
    now = datetime.datetime.now()
    year=now.strftime('%Y')
    month=now.strftime('%m')
    day=now.strftime('%d')
    hour=now.strftime('%H')
    minute=now.strftime('%M')
    second=now.strftime('%S')
    return "users/"+instance.user.username+"/profile/"+year+"/"+month+"/"+day+"/"+hour+"/"+minute+"/"+second+"/profile.jpg"

#DEFINE STUDENT (additional info for each User)
class NewUserProfile(models.Model):
    user = models.OneToOneField(User)
    classYear = models.CharField(choices=yearChoices,max_length=4)
    major = models.CharField(choices=majorChoices, max_length=5)
    livingGroup = models.CharField(choices=livingGroups,max_length=50)#add in choices
    picture= models.ImageField(upload_to=content_file_name, max_length=100, blank=True, null=True)
    skills=models.ManyToManyField(Skill, related_name="Possessors", blank=True, null=True)
    additional = models.TextField(max_length=1000, blank=True, null=True)
    

    def __unicode__(self):
    	return self.user.get_full_name()

    def save(self, *args, **kwargs):
        if not self.pk:
            try:
                p = NewUserProfile.objects.get(user=self.user)
                self.pk = p.pk
            except NewUserProfile.DoesNotExist:
                pass

        super(NewUserProfile, self).save(*args, **kwargs)

#this creates a profile on demand if none exists
def user_post_delete(sender, instance, **kwargs):
    try:
        NewUserProfile.objects.get(user=instance).delete()
    except:
        pass

def user_post_save(sender, instance, **kwargs):
    try:
        profile, new = NewUserProfile.objects.get_or_create(user=instance)
    except:
        pass

models.signals.post_delete.connect(user_post_delete, sender=User)
models.signals.post_save.connect(user_post_save, sender=User)


# editing a profile in the admin
class UserProfileInline(admin.StackedInline):
    model = NewUserProfile
    can_delete = False
    verbose_name_plural = 'profile'

class UserAdmin(UserAdmin):
    inlines = (UserProfileInline, )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Skill)
    