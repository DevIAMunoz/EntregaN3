# En tu aplicación `forms.py`
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class UsuarioForm(UserCreationForm):
    edad = forms.IntegerField(label='Edad')

    class Meta:
        model = CustomUser
        fields = ['username', 'nombre', 'apellido', 'email', 'rut', 'password1', 'edad']
