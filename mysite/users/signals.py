# Signals also need to be registered in apps.py file.

from django.db.models.signals import post_save #To get a signal when user data is saved in register view
from django.contrib.auth.models import User
from django.dispatch import receiver # Importing receiver
from .models import Profile

@receiver(post_save, sender=User) 
def build_profile(sender, instance, created, **kwargs): #Instance is User, created is boolean(if user is created)
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User) 
def save_profile(sender, instance, **kwargs): #created is not sent here as argument, so it just saves.
    instance.profile.save() #there is a one-to-one relationship between User and Profile, the User model has a related Profile object accessible via the profile attribute.