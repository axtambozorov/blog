from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password']


class UserLoginForm(forms.Form):
    username= forms.CharField(max_length=150)
    password = forms.CharField(max_length=128)