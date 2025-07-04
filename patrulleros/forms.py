from django import forms
from .models import Patrullero

class PatrulleroForm(forms.ModelForm):
    class Meta:
        model = Patrullero
        fields = [
            'placa', 'unidad', 'foto', 'conductor', 'latitud_actual',
            'longitud_actual', 'ultimo_reporte', 'telefono_contacto', 'estado_actual',
            'activo'
        ]
        widgets = {
            'ultimo_reporte': forms.DateTimeInput(
                attrs={'type': 'datetime-local'},
                format='%Y-%m-%dT%H:%M'
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Si hay un valor, formatea para el input type="datetime-local"
        if self.instance and self.instance.ultimo_reporte:
            self.initial['ultimo_reporte'] = self.instance.ultimo_reporte.strftime('%Y-%m-%dT%H:%M')
