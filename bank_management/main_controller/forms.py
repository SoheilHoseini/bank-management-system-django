from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=commit)
        Profile.objects.create(user=user)
        return user
