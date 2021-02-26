from django import forms
from django.contrib.auth.models import User
from .models import File
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [ 'username', 'email', 'password1', 'password2']


class FileUploadForm(forms.ModelForm):
    class Meta:
        model = File
        fields = '__all__'
