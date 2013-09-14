from django.db import models

from django.contrib.auth.models import User


# Create your models here.

# DEFINE SKILL


class MessageThread(models.Model):
	post_datetime = models.DateTimeField(auto_now_add=True)
	users = models.ManyToManyField(User)
	userstring= models.CharField(max_length=500)
	
	def save(self, *args, **kwargs):
	    if not self.userstring:
	        self.userstring = "&".join(sorted([user.id for user in self.users]))
	    super(Subject, self).save(*args, **kwargs)
		

class Message(models.Model):
	text = models.CharField(max_length=1000)
	thread = models.ForeignKey(MessageThread, related_name="messages")
	post_datetime = models.DateTimeField(auto_now_add=True)


    