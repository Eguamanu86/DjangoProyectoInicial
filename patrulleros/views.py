from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Patrullero
from .forms import PatrulleroForm
from app.settings import INFORMATION_SYSTEM

class PatrulleroListView(LoginRequiredMixin, ListView):
    model = Patrullero
    template_name = '/patrulleros/patrullero_list.html'
    context_object_name = 'patrulleros'
    paginate_by = 10
    ordering = ['-editadodate']

    def get_queryset(self):
        queryset = super().get_queryset().filter(activo=True)
        placa = self.request.GET.get('placa', '').strip()
        unidad = self.request.GET.get('unidad', '').strip()
        if placa:
            queryset = queryset.filter(placa__icontains=placa)
        if unidad:
            queryset = queryset.filter(unidad__icontains=unidad)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['placa'] = self.request.GET.get('placa', '')
        context['unidad'] = self.request.GET.get('unidad', '')
        context['system'] = INFORMATION_SYSTEM
        context['has_logged_in'] = True
        return context

class PatrulleroDetailView(LoginRequiredMixin, DetailView):
    model = Patrullero
    template_name = 'patrulleros/patrullero_form.html'
    context_object_name = 'patrullero'


class PatrulleroCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Patrullero
    form_class = PatrulleroForm
    template_name = 'patrulleros/patrullero_form.html'
    success_url = reverse_lazy('patrullero_list')
    permission_required = 'patrulleros.add_patrullero'

class PatrulleroUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Patrullero
    form_class = PatrulleroForm
    template_name = 'patrulleros/patrullero_form.html'
    success_url = reverse_lazy('patrullero_list')
    permission_required = 'patrulleros.change_patrullero'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['accion'] = 'Editar Patrullero'
        return context

# borrado fisico
class PatrulleroDeleteViewFisico(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Patrullero
    template_name = 'patrulleros/patrullero_confirm_delete.html'
    success_url = reverse_lazy('patrullero_list')
    permission_required = 'patrulleros.delete_patrullero'

# borrado logico
class PatrulleroDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Patrullero
    template_name = 'patrulleros/patrullero_confirm_delete.html'
    success_url = reverse_lazy('patrullero_list')
    permission_required = 'patrulleros.delete_patrullero'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.activo = False  # Eliminación lógica
        if hasattr(self.object, 'eliminadopor'):
            self.object.eliminadopor = request.user.username
        self.object.save()
        # redireccionar a la lista de patrulleros
        return HttpResponseRedirect(self.success_url)
