from django import forms
from django.forms import ModelForm
from Mascotas.models import MascotaPerdida

import datetime




class MascotaPerdidaForm(ModelForm):

    class Meta:
        model = MascotaPerdida
        fields = ['estado', 'barrio', 'tipo', 'raza', 'fecha', 'nombre', 'mail', 'telefono', 'imagen', 'descripcion']

        widgets = {
            'fecha': forms.SelectDateWidget(years=range(2019, 2021))
        }