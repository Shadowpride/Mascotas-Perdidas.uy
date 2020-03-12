from django import forms
from django.forms import ModelForm
from Mascotas.models import MascotaPerdida
from django.forms.widgets import HiddenInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

import datetime




class MascotaPerdidaForm(ModelForm):

    estado = forms.CharField(initial='PERDIDO', widget = forms.HiddenInput())

    class Meta:
        model = MascotaPerdida
        fields = ['estado', 'barrio', 'tipo', 'raza', 'fecha', 'nombre', 'mail', 'telefono', 'imagen', 'descripcion']

        widgets = {
            'fecha': forms.SelectDateWidget(years=range(2019, 2021)), 
        }

    def clean_fecha(self):                         # <---- para no ingresar fechas mayores a hoy
        fecha_ingreso = self.cleaned_data['fecha']  # <---- me guarda en la variablelo que introduci en 'fecha'

        if fecha_ingreso > datetime.date.today():
            raise forms.ValidationError("Ha ingresado una fecha mayor al día de hoy")

        return fecha_ingreso


class MascotaPerdidaForm_e(ModelForm):

    estado = forms.CharField(initial='ENCONTRADO', widget = forms.HiddenInput())

    class Meta:
        model = MascotaPerdida
        fields = ['estado', 'barrio', 'tipo', 'raza', 'fecha', 'nombre', 'mail', 'telefono', 'imagen', 'descripcion']

        widgets = {
            'fecha': forms.SelectDateWidget(years=range(2019, 2021)), 
        }

    def clean_fecha(self):                         # <---- para no ingresar fechas mayores a hoy
        fecha_ingreso = self.cleaned_data['fecha']  # <---- me guarda en la variablelo que introduci en 'fecha'

        if fecha_ingreso > datetime.date.today():
            raise forms.ValidationError("Ha ingresado una fecha mayor al día de hoy")

        return fecha_ingreso



class CustomUserForm(UserCreationForm):

    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']
