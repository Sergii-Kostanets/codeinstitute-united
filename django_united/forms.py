from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User


class AccountSettingsForm(UserChangeForm):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'Username'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control',
                                       'placeholder': 'Email'})
    )

    class Meta:
        model = User
        fields = ('username', 'email')
