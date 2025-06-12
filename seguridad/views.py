from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views import View
from django.shortcuts import redirect
from django.views.generic import TemplateView
# Create your views here.
class LoginView(View):
    def post(self, request, *args, **kwargs):
        status_code = None
        data = {'success': False}
        try:
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(username=email,password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    data['success'] = True
                    data['user'] = user.username
                    status_code = 200
                else:
                    data['error'] = 'Login Fallido!, usuario no esta habilitado'
                    status_code = 401
            else:
                data['error'] = 'Login Fallido!, credenciales incorrectas.'
                status_code = 400

        except Exception as e:
            data['error'] = str(e)
            status_code = 500

        return JsonResponse(data, status=status_code)

class LoginPageView(TemplateView):
    template_name = 'seguridad/login.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['autor'] = 'UNEMI'
        context['titulo'] = 'Inicio de Sesión'
        context['logo_sistema'] = ''
        context['nombre_sistema'] = 'UNEMI - Sistema de Gestión de Emergencias'
        context['logo_in'] = 'fa fa-graduation-cap fa-3x'
        return context


def logout_user(request):
    logout(request)
    return redirect('/seguridad/login/')
