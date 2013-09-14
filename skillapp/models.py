from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=50)
    uglyname = models.CharField(max_length=50)
    def  __unicode__(self):
        return self.name
    
    def number_of_possessors(self):
    	return self.Possessors.count()

    class Meta:
    	ordering = ['name']
# Create your models here.
