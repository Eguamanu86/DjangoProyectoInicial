from django.urls import path
from seguridad.views import LoginPageView, LoginView, logout_user

urlpatterns = [
    path('login/', LoginPageView.as_view()),
    path('auth/', LoginView.as_view()),
    path('salir/', logout_user),
]
