from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    """A form to register a new user.
    """
    email = forms.EmailField()

    class Meta:
        """Meta class to specify the model and fields to include in the form.
        """
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileEditForm(forms.ModelForm):
    """A form to edit a user's profile.
    """
    class Meta:
        model = Profile
        fields = ['bio', 'phone_number', 'organisation', 'position', 'profile_picture']