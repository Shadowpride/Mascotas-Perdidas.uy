
from django.contrib import admin
from django.urls import path, include
from .views import home, nuevo_ingreso_perdido, nuevo_ingreso_encontrado, Listado_publicaciones, Modificar_publicaciones, Eliminar_publicacion, Ver_publicacion, registro_usuario, historial, Finalizar, Verificar_publicaciones_subidas

# ------   PARA MANIPULAR IMAGENES   ------ #

from django.conf import settings
from django.conf.urls.static import static

# ----------------------------------------- #


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # <---- para acceder al login
    path('', home, name="home"),
    path('nuevo_ingreso_perdido/', nuevo_ingreso_perdido, name='nuevo_ingreso_perdido'),
    path('nuevo_ingreso_encontrado/', nuevo_ingreso_encontrado, name='nuevo_ingreso_encontrado'),
    path('verificar_publicacion_subida/', Verificar_publicaciones_subidas, name='verificar_publicacion'),
    path('listado_publicaciones/', Listado_publicaciones, name='listado_publicaciones'),
    path('modificar_publicaciones/<id>/', Modificar_publicaciones, name='modificar_publicaciones'),
    path('eliminar_publicacion/<id>/', Eliminar_publicacion, name='eliminar_publicacion'),
    path('finalizar/<id>/', Finalizar, name='finalizar'),
    path('ver_publicacion/<id>/', Ver_publicacion, name='ver_publicacion'),
    path('registro/', registro_usuario, name='registro_usuario'),
    path('historial/', historial, name='historial'),
]


# ------   PARA MANIPULAR IMAGENES   ------ #

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# ----------------------------------------- #


# ------   edita visualmente el administrador de Django   ------ #

admin.site.site_header = 'Administración de Mascotas Perdidas'
admin.site.index_title = 'Modulos de Administracion'
admin.site.index_title = 'Mascotas Perdidas'

# -------------------------------------------------------------- #