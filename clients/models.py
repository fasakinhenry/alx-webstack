from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """A model to store additional information about a user.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='clients_profile')
    bio = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    organisation = models.CharField(max_length=255, blank=True, null=True)
    position = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        """Return a string representation of the model instance.
        """
        return f"{self.user.username}'s profile"