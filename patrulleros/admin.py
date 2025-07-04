from django.contrib import admin
from .models import Patrullero, AsignacionRespuesta

class PatrulleroAdmin(admin.ModelAdmin):
    list_display = ('placa', 'unidad', 'conductor', 'telefono_contacto', 'estado_actual', 'activo')
    list_per_page = 20
    ordering = ('-id',)
    search_fields = ('placa', 'unidad', 'conductor', 'telefono_contacto')
    list_filter = ('estado_actual', 'activo')

    def estado(self, obj):
        return obj.activo
    estado.boolean = True

class AsignacionRespuestaAdmin(admin.ModelAdmin):
    list_display = ('patrullero', 'reporte', 'estado', 'fecha_asignacion', 'activo')
    list_per_page = 20
    ordering = ('-id',)
    search_fields = ('patrullero__placa', 'reporte__id')
    list_filter = ('estado', 'activo')

    def estado(self, obj):
        return obj.activo
    estado.boolean = True

admin.site.register(Patrullero, PatrulleroAdmin)
admin.site.register(AsignacionRespuesta, AsignacionRespuestaAdmin)
