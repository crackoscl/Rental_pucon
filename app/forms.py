from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db.models.base import Model
from django.forms import TextInput,EmailInput,PasswordInput,Textarea,DateTimeInput
from .models import Usuarios,Arriendos


class RegisterUserForm(UserCreationForm):
    
    class Meta:
        model = Usuarios
        fields = ['username','email','rut']
        widgets = {
        'username': TextInput(attrs={'class':'form-control','placeholder': 'Nombre Usuario'}),
        'email': EmailInput(attrs={'class':'form-control','placeholder': 'Email'}),
        'rut': TextInput(attrs={'class':'form-control','placeholder': 'Rut'}),
    }
    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'})
        self.fields['password2'].widget = PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmacion Contraseña'})


class ArrendarForm(forms.ModelForm):
    class Meta:
        model = Arriendos
        fields= ['observaciones']
        widgets = {
        'observaciones': Textarea(attrs={'class':'form-control'}),
    }      


