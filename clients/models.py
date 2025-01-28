from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """A model to store additional information about a user.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='clients_profile')
    bio = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    organisation = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    position = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        """Return a string representation of the model instance.
        """
        return f"{self.user.username}'s profile"



class Message(models.Model):
    """A model to store messages between users."""
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender.username} to {self.recipient.username} at {self.timestamp}"
