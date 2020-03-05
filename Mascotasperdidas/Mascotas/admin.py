from django.contrib import admin
from .models import Estado, Barrio, Tipo, Raza, MascotaPerdida




class EstadoAdmin(admin.ModelAdmin):
    list_filter = ['situacion']
    list_per_page = 20


class BarrioAdmin(admin.ModelAdmin):
    list_filter = ['lugar']
    list_per_page = 20


class TipoAdmin(admin.ModelAdmin):
    list_filter = ['especie']
    list_per_page = 20


class RazaAdmin(admin.ModelAdmin):
    list_filter = ['tipo']
    list_per_page = 20


class MascotaPerdidaAdmin(admin.ModelAdmin):
    list_display = ['estado', 'barrio', 'tipo', 'raza']
    search_fields = ['nombre', 'mail', 'telefono', 'descripcion']
    list_filter = ['estado']
    list_per_page = 20


admin.site.register(Estado, EstadoAdmin)
admin.site.register(Barrio, BarrioAdmin)
admin.site.register(Tipo, TipoAdmin)
admin.site.register(Raza, RazaAdmin)
admin.site.register(MascotaPerdida, MascotaPerdidaAdmin)
