"""Mascotasperdidas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import home, nuevo_ingreso_perdido, nuevo_ingreso_encontrado, Listado_publicaciones, Modificar_publicaciones, Eliminar_publicacion

# ------   PARA MANIPULAR IMAGENES   ------ #

from django.conf import settings
from django.conf.urls.static import static

# ----------------------------------------- #


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('nuevo_ingreso_perdido/', nuevo_ingreso_perdido, name='nuevo_ingreso_perdido'),
    path('nuevo_ingreso_encontrado/', nuevo_ingreso_encontrado, name='nuevo_ingreso_encontrado'),
    path('listado_publicaciones/', Listado_publicaciones, name='listado_publicaciones'),
    path('modificar_publicaciones/<id>/', Modificar_publicaciones, name='modificar_publicaciones'),
    path('eliminar_publicacion/<id>/', Eliminar_publicacion, name='eliminar_publicacion'),
]


# ------   PARA MANIPULAR IMAGENES   ------ #

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# ----------------------------------------- #


# ------   edita visualmente el administrador de Django   ------ #

admin.site.site_header = 'Administración de Mascotas Perdidas'
admin.site.index_title = 'Modulos de Administracion'
admin.site.index_title = 'Mascotas Perdidas'

# -------------------------------------------------------------- #