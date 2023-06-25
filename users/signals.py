from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    Signal receiver function to create a profile for a newly created user.

    Args:
        sender: The model class that sent the signal (User).
        instance: The actual instance of the model (User instance).
        created (bool): Flag indicating whether the user was created or not.
        **kwargs: Additional keyword arguments.

    Returns:
        None

    """
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    """
    Signal receiver function to save the profile when a user is saved.

    Args:
        sender: The model class that sent the signal (User).
        instance: The actual instance of the model (User instance).
        **kwargs: Additional keyword arguments.

    Returns:
        None

    """
    instance.profile.save()
