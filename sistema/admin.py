from django.contrib import admin
from .models import Pais, Provincia, Ciudad
# Register your models here.
class PaisAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'estado')
    search_fields = ('nombre',)
    ordering = ('-editadodate',)
    list_filter = ('activo',)
    def estado(self, obj):
        return obj.activo
    estado.boolean = True

class ProvinciaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais', 'estado')
    search_fields = ('nombre', 'pais__nombre')
    ordering = ('-editadodate',)
    list_filter = ('activo', 'pais__nombre')
    def estado(self, obj):
        return obj.activo
    estado.boolean = True

class CiudadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'provincia', 'estado')
    search_fields = ('nombre', 'provincia__nombre')
    ordering = ('-editadodate',)
    list_filter = ('activo', 'provincia__nombre')
    autocomplete_fields = ('provincia',)
    def estado(self, obj):
        return obj.activo
    estado.boolean = True

admin.site.register(Pais, PaisAdmin)
admin.site.register(Provincia, ProvinciaAdmin)
admin.site.register(Ciudad, CiudadAdmin)
