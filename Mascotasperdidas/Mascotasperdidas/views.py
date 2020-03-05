from django.shortcuts import render
from Mascotas.models import MascotaPerdida
from .forms import MascotaPerdidaForm




def home(request):
    mascotas = MascotaPerdida.objects.all()
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
    return render(request, 'nuevo_ingreso_perdido.html', data)


def nuevo_ingreso_encontrado(request):
    data = {
        'form':MascotaPerdidaForm()                                         # <---- formulario vacio para rellenar
    }

    if request.method == 'POST':                                            # <---- si enviamos elementos de formulario entra en el 'if'
        formulario = MascotaPerdidaForm(request.POST, files=request.FILES)  # <---- metemos los elementos en el formulario
        if formulario.is_valid():
            formulario.save()                                               # <---- si se validan los datos, se guarda y se envia al servidor
            data['mensaje'] = "Publicacion Guardada Correctamente"
    return render(request, 'nuevo_ingreso_encontrado.html', data)