from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm

class UserCreationForm(BaseUserCreationForm):
    class Meta(BaseUserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'password1', 'password2', 'role')
