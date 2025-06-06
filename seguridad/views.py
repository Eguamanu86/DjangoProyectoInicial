from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views import View
from django.shortcuts import redirect
# Create your views here.
class LoginView(View):
    def post(self, request, *args, **kwargs):
        data = {'resp': False}
        try:
            cuenta = str(request.POST.get('usuario')).strip()
            user = authenticate(username=cuenta,password=request.POST['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    data['resp'] = True
                    data['user'] = user.username
                    return JsonResponse(data, status=200)
                else:
                    data['error'] = 'Login Fallido!, usuario no esta habilitado'
            else:
                data['error'] = 'Login Fallido!, credenciales incorrectas.'

        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, status=200)

    def put(self, request, *args, **kwargs):
        data = {'resp': False}
        try:
            cuenta = str(request.POST.get('usuario')).strip()
            user = authenticate()
            if user is not None:
                if user.is_active:
                    login(request, user)
                    data['resp'] = True
                    data['user'] = user.username
                    return JsonResponse(data, status=200)
                else:
                    data['error'] = 'Login Fallido!, usuario no esta habilitado'
            else:
                data['error'] = 'Login Fallido!, credenciales incorrectas.'

        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, status=200)


def logout_user(request):
    logout(request)
    return redirect('/seguridad/login/')
