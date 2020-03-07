from django.shortcuts import render
from Mascotas.models import MascotaPerdida
from .forms import MascotaPerdidaForm, MascotaPerdidaForm_e


def home(request):
    mascotas = MascotaPerdida.objects.order_by('-id')                       # <---- mostrar ultimos anuncios al principio
    data = {
        'mascotas':mascotas
    }
    return render(request, 'home.html', data)


def nuevo_ingreso_perdido(request):
    data = {
        'form':MascotaPerdidaForm()                                         # <---- formulario vacio para rellenar
    }

    if request.method == 'POST':                                            # <---- si enviamos elementos de formulario entra en el 'if'
        formulario = MascotaPerdidaForm(request.POST, files=request.FILES)  # <---- metemos los elementos en el formulario
       
        if formulario.is_valid():
            formulario.save()                                               # <---- si se validan los datos, se guarda y se envia al servidor
            data['mensaje'] = "Publicacion Guardada Correctamente"
        data['form'] = formulario                                           # <---- para ingresar las validaciones .forms.py> Alerta_fecha
    return render(request, 'nuevo_ingreso_perdido.html', data)


def nuevo_ingreso_encontrado(request):
    data = {
        'form_e':MascotaPerdidaForm_e()                                         # <---- formulario vacio para rellenar
    }

    if request.method == 'POST':                                            # <---- si enviamos elementos de formulario entra en el 'if'
        formulario_e = MascotaPerdidaForm_e(request.POST, files=request.FILES)  # <---- metemos los elementos en el formulario

        if formulario_e.is_valid():
            formulario_e.save()                                               # <---- si se validan los datos, se guarda y se envia al servidor
            data['mensaje'] = "Publicacion Guardada Correctamente"
        data['form_e'] = formulario_e
    return render(request, 'nuevo_ingreso_encontrado.html', data)
