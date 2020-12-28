from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from.models import Person,Comment

class PersonForm(ModelForm):
    class Meta:
        model=Person
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class CommentForm(ModelForm):
    class Meta:
        model=Comment
        fields = ['comment']