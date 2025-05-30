from django.contrib import admin
from .models import Reporte

class ReporteAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'fecha_hora', 'anonimo', 'prioridad', 'activo')
    search_fields = ('tipo', 'descripcion')
    ordering = ('-fecha_hora',)
    list_filter = ('anonimo', 'prioridad', 'activo')

admin.site.register(Reporte, ReporteAdmin)
