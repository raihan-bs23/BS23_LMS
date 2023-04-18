from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.db import models
from .models import UserAdditionalInfo

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',

        ]

class UserAdditionalInfoForm(forms.ModelForm):
    class Meta:
        model = UserAdditionalInfo
        fields = [
            'username',
            'user_full_name',
            'contact_no',
            'profession',
            'user_role',
            'profile_picture',
            'social_link',
        ]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['username'].initial = user.username

