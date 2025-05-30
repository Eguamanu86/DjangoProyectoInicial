from django.contrib import admin
from .models import Zona, Ubicacion

class ZonaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ciudad', 'nivel_riesgo', 'estado')
    search_fields = ('nombre', 'ciudad__nombre')
    ordering = ('-id',)
    list_filter = ('nivel_riesgo', 'ciudad', 'activo')
    autocomplete_fields = ('ciudad',)
    def estado(self, obj):
        return obj.activo
    estado.boolean = True

class UbicacionAdmin(admin.ModelAdmin):
    list_display = ('direccion', 'zona', 'zona_riesgo', 'timestamp')
    search_fields = ('direccion', 'zona__nombre')
    ordering = ('-timestamp',)
    list_filter = ('zona_riesgo', 'zona')

admin.site.register(Zona, ZonaAdmin)
admin.site.register(Ubicacion, UbicacionAdmin)
