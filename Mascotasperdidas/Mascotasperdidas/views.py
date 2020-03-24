from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required  # <---- Para pedir acceso de login a funcionalidades
from Mascotas.models import MascotaPerdida, Barrio, Raza
from .forms import MascotaPerdidaForm, MascotaPerdidaForm_e, CustomUserForm
from django.contrib.auth import login, authenticate




def home(request):
    mascotas = MascotaPerdida.objects.order_by('-id')                       # <---- mostrar ultimos anuncios al principio
    barrios = Barrio.objects.all()
    razaotros = Raza.objects.filter(tipo='OTRO')
    razasperros = Raza.objects.filter(id__gte=6, id__lte=15)
    razasgatos = Raza.objects.filter(id__gte=16)

    data = {
        'mascotas':mascotas,
        'barrios':barrios,
        'razaotros':razaotros,
        'razasperros':razasperros,
        'razasgatos':razasgatos
    }

    if request.method == 'POST':
        filtro_estado = request.POST.get('filtro_estado')
        filtro_tipo = request.POST.get('filtro_tipo')
        filtro_barrio = request.POST.get('filtro_barrio')
        filtro_raza = request.POST.get('filtro_raza')
        
        if filtro_estado == '' and filtro_tipo == '' and filtro_barrio == '' and filtro_raza =='':
            pass
        
        elif filtro_estado !='' and filtro_tipo =='' and filtro_barrio == '' and filtro_raza =='':
            mascotas = MascotaPerdida.objects.order_by('-id').filter(estado=filtro_estado)
            data['mascotas'] = mascotas
        
        elif filtro_estado !='' and filtro_tipo =='' and filtro_barrio == '' and filtro_raza !='':
            mascotas = MascotaPerdida.objects.order_by('-id').filter(estado=filtro_estado, raza_id=filtro_raza)
            data['mascotas'] = mascotas

        elif filtro_estado !='' and filtro_tipo !='' and filtro_barrio =='' and filtro_raza =='':
            mascotas = MascotaPerdida.objects.order_by('-id').filter(estado=filtro_estado, tipo_id=filtro_tipo)
            data['mascotas'] = mascotas

        elif filtro_estado !='' and filtro_tipo !='' and filtro_barrio =='' and filtro_raza !='':
            mascotas = MascotaPerdida.objects.order_by('-id').filter(estado=filtro_estado, tipo_id=filtro_tipo, raza_id=filtro_raza)
            data['mascotas'] = mascotas

        elif filtro_estado == '' and filtro_tipo !='' and filtro_barrio =='' and filtro_raza =='':
            mascotas = MascotaPerdida.objects.order_by('-id').filter(tipo_id=filtro_tipo)
            data['mascotas'] = mascotas

        elif filtro_estado == '' and filtro_tipo !='' and filtro_barrio !='' and filtro_raza =='':
            mascotas = MascotaPerdida.objects.order_by('-id').filter(tipo_id=filtro_tipo, barrio_id=filtro_barrio)
            data['mascotas'] = mascotas

        elif filtro_estado != '' and filtro_tipo =='' and filtro_barrio !='' and filtro_raza =='':
            mascotas = MascotaPerdida.objects.order_by('-id').filter(estado=filtro_estado, barrio_id=filtro_barrio)
            data['mascotas'] = mascotas

        elif filtro_estado != '' and filtro_tipo =='' and filtro_barrio !='' and filtro_raza !='':
            mascotas = MascotaPerdida.objects.order_by('-id').filter(estado=filtro_estado, barrio_id=filtro_barrio, raza_id=filtro_raza)
            data['mascotas'] = mascotas
            
        elif filtro_estado == '' and filtro_tipo =='' and filtro_barrio !='' and filtro_raza =='':
            mascotas = MascotaPerdida.objects.order_by('-id').filter(barrio_id=filtro_barrio)
            data['mascotas'] = mascotas

        elif filtro_estado == '' and filtro_tipo =='' and filtro_barrio =='' and filtro_raza !='':
            mascotas = MascotaPerdida.objects.order_by('-id').filter(raza_id=filtro_raza)
            data['mascotas'] = mascotas

        elif filtro_estado == '' and filtro_tipo !='' and filtro_barrio =='' and filtro_raza !='':
            mascotas = MascotaPerdida.objects.order_by('-id').filter(tipo_id=filtro_tipo, raza_id=filtro_raza)
            data['mascotas'] = mascotas

        elif filtro_estado == '' and filtro_tipo !='' and filtro_barrio !='' and filtro_raza !='':
            mascotas = MascotaPerdida.objects.order_by('-id').filter(tipo_id=filtro_tipo, barrio_id=filtro_barrio, raza_id=filtro_raza)
            data['mascotas'] = mascotas

        elif filtro_estado == '' and filtro_tipo =='' and filtro_barrio !='' and filtro_raza !='':
            mascotas = MascotaPerdida.objects.order_by('-id').filter(barrio_id=filtro_barrio, raza_id=filtro_raza)
            data['mascotas'] = mascotas
        
        elif filtro_estado !='' and filtro_tipo !='' and filtro_barrio !='' and filtro_raza =='':
            mascotas = MascotaPerdida.objects.order_by('-id').filter(estado=filtro_estado, tipo_id=filtro_tipo, barrio_id=filtro_barrio)
            data['mascotas'] = mascotas

        else:
            mascotas = MascotaPerdida.objects.order_by('-id').filter(estado=filtro_estado,
                                                                    tipo_id=filtro_tipo,
                                                                    barrio_id=filtro_barrio,
                                                                    raza_id=filtro_raza)
            data['mascotas'] = mascotas

    return render(request, 'home.html', data)


@login_required
def nuevo_ingreso_perdido(request):
    data = {
        'form':MascotaPerdidaForm()                                         # <---- formulario vacio para rellenar
    }

    if request.method == 'POST':                                            # <---- si enviamos elementos de formulario entra en el 'if'
        formulario = MascotaPerdidaForm(request.POST, files=request.FILES)  # <---- metemos los elementos en el formulario
       
        if formulario.is_valid():
            formulario.save()                                               # <---- si se validan los datos, se guarda y se envia al servidor
            return redirect(to='verificar_publicacion')
        data['form'] = formulario                                           # <---- para ingresar las validaciones .forms.py> Alerta_fecha
    return render(request, 'nuevo_ingreso_perdido.html', data)


@login_required
def nuevo_ingreso_encontrado(request):
    data = {
        'form_e':MascotaPerdidaForm_e()                                         # <---- formulario vacio para rellenar
    }

    if request.method == 'POST':                                            # <---- si enviamos elementos de formulario entra en el 'if'
        formulario_e = MascotaPerdidaForm_e(request.POST, files=request.FILES)  # <---- metemos los elementos en el formulario

        if formulario_e.is_valid():
            formulario_e.save()                                               # <---- si se validan los datos, se guarda y se envia al servidor
            return redirect(to='verificar_publicacion')
        data['form_e'] = formulario_e
    return render(request, 'nuevo_ingreso_encontrado.html', data)


def Verificar_publicaciones_subidas(request):
    return render(request, 'verificar_publicacion_subida.html')


@login_required
def Listado_publicaciones(request):
    listado = MascotaPerdida.objects.order_by('-id')
    data = {
        'listado': listado
    }
    return render(request, 'listado_publicaciones.html', data)


def Modificar_publicaciones(request, id):
    modificar = MascotaPerdida.objects.get(id=id)
    data = {
        'form': MascotaPerdidaForm(instance=modificar)
    }

    if request.method == 'POST':
        formulario = MascotaPerdidaForm(data=request.POST, files=request.FILES, instance=modificar)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='listado_publicaciones')
        data['form'] = formulario

    return render(request, 'modificar_publicaciones.html', data)


def Eliminar_publicacion(request, id):
    publicacion = MascotaPerdida.objects.get(id=id)
    publicacion.delete()

    return redirect(to="listado_publicaciones")


def Finalizar(request, id):
    publicacion = MascotaPerdida.objects.get(id=id)
    publicacion.estado='FINALIZADO'              #Cambia estado a FINALZIADO
    publicacion.save()

    return redirect(to="listado_publicaciones")


def Ver_publicacion(request, id):
    publicacion = MascotaPerdida.objects.get(id=id)
    data = {
        'publicacion': publicacion
    }
    return render(request, 'ver_publicacion.html', data)


def registro_usuario(request):
    data = {
        'form': CustomUserForm()
    }

    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            #autenticar al usuario y redirigir al inicio
            email = formulario.cleaned_data['email']
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(email=email, username=username, password=password)
            login(request, user)
            return redirect(to='home')

    return render(request, 'registration/registrar.html', data)


def historial(request):
    historial = MascotaPerdida.objects.order_by('fecha')                      # <---- mostrar ultimos anuncios al principio
    data = {
        'historial':historial
    }
    return render(request, 'historial.html', data)