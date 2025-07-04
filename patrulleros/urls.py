from django.urls import path
from .views import (
    PatrulleroListView, PatrulleroDetailView,
    PatrulleroCreateView, PatrulleroUpdateView, PatrulleroDeleteView, PatrulleroDeleteViewFisico
)

urlpatterns = [
    path('', PatrulleroListView.as_view(), name='patrullero_list'),
    path('add/', PatrulleroCreateView.as_view(), name='patrullero_create'),
    path('<int:pk>/', PatrulleroDetailView.as_view(), name='patrullero_detail'),
    path('<int:pk>/update/', PatrulleroUpdateView.as_view(), name='patrullero_update'),
    path('<int:pk>/delete/logico/', PatrulleroDeleteView.as_view(), name='patrullero_delete_logico'),
    path('<int:pk>/delete/fisico/', PatrulleroDeleteViewFisico.as_view(), name='patrullero_delete_fisico'),
]
