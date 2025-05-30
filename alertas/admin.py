from django.contrib import admin
from .models import Alerta

class AlertaAdmin(admin.ModelAdmin):
    list_display = ('tipo_alerta', 'nivel_urgencia', 'fecha_hora', 'resuelta', 'estado')
    list_per_page = 20
    search_fields = ('tipo_alerta',)
    ordering = ('-fecha_hora',)
    list_filter = ('resuelta', 'nivel_urgencia')
    def estado(self, obj):
        return not obj.activo
    estado.boolean = True

admin.site.register(Alerta, AlertaAdmin)
