from django.contrib import admin
from .models import EventoSistema

class EventoSistemaAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'origen', 'tipo', 'fecha_hora', 'usuario')
    list_per_page = 20
    ordering = ('-fecha_hora',)
    search_fields = ('descripcion', 'usuario__username', 'origen', 'tipo')
    list_filter = ('origen', 'tipo', 'fecha_hora')

admin.site.register(EventoSistema, EventoSistemaAdmin)
