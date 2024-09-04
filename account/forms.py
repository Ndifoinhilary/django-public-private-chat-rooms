from django import forms
from django.contrib.auth.forms import UserCreationForm

from account.models import Account


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta:
        model = Account
        fields = ('email', 'username', 'password1', 'password2')


    def clean_email(self):
        email = self.cleaned_data.get('email').lower()
        try:
            account = Account.objects.get(email=email)
        except Exception as e:
            return email
        raise forms.ValidationError(f"Sorry an account with the email {email} already exist.")


    def clean_username(self):
        username = self.cleaned_data.get('username').lower()
        try:
            account = Account.objects.get(username=username)
        except Exception as e:
            return username
        raise forms.ValidationError(f"Sorry an account with the username {username} already exist.")


