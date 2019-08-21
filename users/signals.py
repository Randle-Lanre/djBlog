#signals when a model is saved
#the main goal of this file is to be able to trigger 
#so that when a user is created we automatally attach the 
#user with a profile (i.e create a profile)
from django.db.models.signals import post_save
from django.contrib.auth.models import User 
#we also need to import a reciever since we already have a signal/sender already
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

#**kwags just accepts anyother additional parameters	

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
	instance.profile.save()

#we also have to now import this signal file into the app.py file so that it can work 