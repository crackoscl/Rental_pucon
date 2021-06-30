import re
from itertools import cycle
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.forms import TextInput, EmailInput, PasswordInput, Textarea
from .models import Arriendos

User = get_user_model()


class RegisterUserForm(UserCreationForm):

    def clean_username(self):
        username = self.cleaned_data['username']
        existe = User.objects.filter(username__iexact=username).exists()
        if existe:
            raise ValidationError('Este nombre de usuario ya existe')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            match = User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise ValidationError('Este Email ya existe')

    def clean_rut(self):
        rut_clean = (
            re.sub("[^0-9kK]", "", str(self.cleaned_data.get('rut')))).lower()
        if rut_clean.count("k") > 0:
            if rut_clean.count("k") > 1 or rut_clean[-1] != "k":
                raise ValidationError("formato de RUT incorrecto")
        if len(rut_clean) < 8 or len(rut_clean) > 9:
            raise ValidationError(
                "El número de digitos ingresados no es correcto!")
        rut_clean_no_digit = int(rut_clean[:-1])
        reversed_digits = map(int, reversed(str(rut_clean_no_digit)))
        factors = cycle(range(2, 8))
        s = sum(d * f for d, f in zip(reversed_digits, factors))
        digit = (-s) % 11
        if digit == 10:
            digit = "k"
        if str(digit) == rut_clean[-1]:
            return rut_clean
        else:
            raise ValidationError("El Digito Verificador no corresponde!")

    class Meta:
        model = User
        fields = ['username', 'email', 'rut']
        widgets = {
            'username': TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre Usuario'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'rut': TextInput(attrs={'class': 'form-control', 'placeholder': 'Rut'}),
        }

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Contraseña'})
        self.fields['password2'].widget = PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Confirmación Contraseña'})
        self.fields['email'].required = True


class ArrendarForm(forms.ModelForm):
    class Meta:
        model = Arriendos
        fields = ['observaciones']
        widgets = {
            'observaciones': Textarea(attrs={'class': 'form-control'}),
        }
