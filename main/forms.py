from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *


class CreateActorForm(UserCreationForm):
    class Meta:
        model = Actor
        fields = {'username', 'email', 'password1', 'password2'}


class CreateEmployerForm(UserCreationForm):
    class Meta:
        model = Employer
        fields = {'username', 'email', 'password1', 'password2'}


class ActorModelForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = ['name', 'education', 'location', 'birth_date', 'sex', 'weight', 'height', 'eye_color',
                  'hair_color', 'race', 'nation', 'body_type']


class EmployerModelForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = ['name', 'organization', 'position']


class RoleModelForm(forms.ModelForm):
    class Meta:
        model = Role
        exclude = ['creator']
