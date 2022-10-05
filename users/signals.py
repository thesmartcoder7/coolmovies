from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

"""
post_save is a signal that gets fired when an object is saved
in line 2, the User model that is being imported is what is going
to be the sender since it is going to be sending the post_save signal

the receiver being imported is what will be used to create the receiver
funcition for receiving the signal sent from the User after a user
has been saved successfully 

"""

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)



@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
