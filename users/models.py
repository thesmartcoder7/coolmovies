from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Model representing a user profile.

    Attributes:
        user (OneToOneField): The user associated with the profile.
        image (ImageField): The profile image of the user.

    Methods:
        __str__: Returns a string representation of the profile.

    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        """
        Returns a string representation of the profile.

        Returns:
            str: The username followed by 'Profile'.

        """
        return f'{self.user.username} Profile'
