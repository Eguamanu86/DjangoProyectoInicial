from django.contrib import admin
from .models import DispositivoIoT

class DispositivoIoTAdmin(admin.ModelAdmin):
    list_display = ('codigo_serie', 'tipo', 'estado', 'estado_conexion', 'ultimo_ping', 'centro_monitoreo')
    search_fields = ('codigo_serie',)
    ordering = ('-fecha_instalacion',)
    list_filter = ('tipo', 'estado', 'estado_conexion')

admin.site.register(DispositivoIoT, DispositivoIoTAdmin)
