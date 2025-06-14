from django.urls import path
from seguridad.views import LoginPageView, LoginView, logout_user

urlpatterns = [
    path('login/', LoginPageView.as_view()), # Formulario de inicio de sesión
    path('auth/', LoginView.as_view()),# URL para autenticación
    path('salir/', logout_user), # URL para cerrar sesión
]
