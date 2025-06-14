from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views import View
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from app.settings import INFORMATION_SYSTEM
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
                    login(request, user) # Activa la sesión del usuario
                    data['success'] = True
                    status_code = 200 # OK
                else:
                    data['error'] = 'Login Fallido!, usuario no esta habilitado'
                    status_code = 401 # Unauthorized
            else:
                data['error'] = 'Login Fallido!, credenciales incorrectas.'
                status_code = 400 # Bad Request

        except Exception as e:
            data['error'] = str(e)
            status_code = 500 # Internal Server Error

        return JsonResponse(data, status=status_code)

class LoginPageView(TemplateView):
    template_name = 'seguridad/login.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['system'] = INFORMATION_SYSTEM
        context['has_logged_in'] = False

        return context

class IndexPageView(LoginRequiredMixin, TemplateView):
    template_name = 'seguridad/index.html'
    login_url = '/seguridad/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['system'] = INFORMATION_SYSTEM
        context['has_logged_in'] = True
        return context

def logout_user(request):
    logout(request)
    return redirect('/seguridad/login/')
