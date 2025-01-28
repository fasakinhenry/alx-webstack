from django import forms
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    """A form to register a new user."""
    email = forms.EmailField()

    class Meta:
        """Meta class to specify the model and fields to include in the form."""
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control custom-form-control'
            field.widget.attrs['placeholder'] = field.label

class ProfileEditForm(forms.ModelForm):
    """A form to edit a user's profile."""
    class Meta:
        model = Profile
        fields = ['bio', 'phone_number', 'email', 'address', 'full_name', 'skills', 'profile_picture']

    def __init__(self, *args, **kwargs):
        super(ProfileEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control custom-form-control'
            field.widget.attrs['placeholder'] = field.label