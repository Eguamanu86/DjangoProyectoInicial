from django.contrib import admin
from .models import CentroMonitoreo

class CentroMonitoreoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'coordinador', 'telefono', 'estado')
    list_per_page = 20
    ordering = ('-id',)
    search_fields = ('nombre', 'coordinador')
    list_filter = ('activo',)

    def estado(self, obj):
        return obj.activo
    estado.boolean = True

admin.site.register(CentroMonitoreo, CentroMonitoreoAdmin)
