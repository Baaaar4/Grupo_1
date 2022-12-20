from django import forms
from django.forms import ModelForm

from castillo_barbara.models import Idea, Pensamiento


class IdeaForm(ModelForm):
    class Meta:
        model = Idea
        fields = ['idea']

class PensamientoForm(ModelForm):
    class Meta:
        model = Pensamiento
        fields = ['idea' ]


class LoginForm(forms.Form):
    email = forms.CharField(
        max_length=250, min_length=3, label='Ingrese su nombre de usuario')
    password = forms.CharField(min_length=8, max_length=16,
                               label='Ingrese su contraseña', widget=forms.PasswordInput())
