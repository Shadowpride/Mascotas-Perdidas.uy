from django import forms
from django.forms import ModelForm
from Mascotas.models import MascotaPerdida
from django.forms.widgets import HiddenInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required 

import datetime




class MascotaPerdidaForm(ModelForm):

    estado = forms.CharField(initial='PERDIDO', widget = forms.HiddenInput())
    imagen = forms.ImageField(required=True)

    class Meta:
        model = MascotaPerdida
        fields = ['estado', 'barrio', 'tipo', 'raza', 'fecha', 'nombre', 'mail', 'telefono', 'imagen', 'descripcion']

        widgets = {
            'fecha': forms.SelectDateWidget(years=range(2020, 2021)), 
        }

    def clean_fecha(self):                         # <---- para no ingresar fechas mayores a hoy
        fecha_ingreso = self.cleaned_data['fecha']  # <---- me guarda en la variablelo que introduci en 'fecha'

        if fecha_ingreso > datetime.date.today():
            raise forms.ValidationError("Ha ingresado una fecha mayor al día de hoy")

        return fecha_ingreso


class MascotaPerdidaForm_e(ModelForm):

    estado = forms.CharField(initial='ENCONTRADO', widget = forms.HiddenInput())
    imagen = forms.ImageField(required=True)

    class Meta:
        model = MascotaPerdida
        fields = ['estado', 'barrio', 'tipo', 'raza', 'fecha', 'nombre', 'mail', 'telefono', 'imagen', 'descripcion']

        widgets = {
            'fecha': forms.SelectDateWidget(years=range(2020, 2021)), 
        }

    def clean_fecha(self):                         # <---- para no ingresar fechas mayores a hoy
        fecha_ingreso = self.cleaned_data['fecha']  # <---- me guarda en la variablelo que introduci en 'fecha'

        if fecha_ingreso > datetime.date.today():
            raise forms.ValidationError("Ha ingresado una fecha mayor al día de hoy")

        return fecha_ingreso



class CustomUserForm(UserCreationForm):

    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True, label="Nombre")
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']
