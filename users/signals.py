'''This signals.py is for generating post_save signal after the user is created, 
so that it automatically creates and saves profile pic as well'''
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
from django.db.models.signals import post_save

'''here, User sends the post_save signal to the receiver create_profile and creates the profile'''
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

'''after creating profile, it must be saved, then go to apps.py'''
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
	instance.profile.save()