from django import forms
from django.contrib.auth.hashers import make_password

class ClientForm(forms.Form):
    user_name = forms.CharField(
            max_length = 100,
            widget = forms.TextInput(attrs={'placeholder': 'User Name'}),
            label = "Username"
            )

    first_name = forms.CharField(
            max_length = 100,
            widget = forms.TextInput(attrs={'placeholder': 'Full Name'}),
            label = "Full name"
            )
    second_name = forms.CharField(
            max_length = 100,
            widget = forms.TextInput(attrs={'placeholder': 'Second Name'}),
            label = "second name"
            )
    email = forms.CharField(
            max_length = 100,
            widget = forms.EmailInput(attrs={'placeholder': 'Email'}),
            label = "email"
            )
    age = forms.IntegerField(
        widget = forms.NumberInput(attrs={'placeholder':'How old are you'}),
        label = 'age',
        min_value =  1
        )
    phone = forms.CharField(
            max_length = 100,
            widget = forms.TextInput(attrs={'placeholder': 'phone'}),
            label = "phone"
            )
    service_neede = forms.CharField(
            max_length = 100,
            widget = forms.TextInput(attrs={'placeholder': 'service needed'}),
            label = "service needed"
            )
    address = forms.CharField(
            widget = forms.TextInput(attrs={'placeholder': 'address', 'rows':3}),
            label = "address"
            )
    password = forms.CharField(
            widget = forms.PasswordInput(attrs={'placeholder': 'password'}),
            label = "password",
            help_text = "password must be at least 8 charelacter long."
            )
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError("password must be at least 8 character long.")
        return make_password(password)


