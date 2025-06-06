from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views import View
from django.shortcuts import redirect
# Create your views here.
class LoginView(View):
    def post(self, request, *args, **kwargs):
        """
        Authenticates a user based on provided username and password and logs them in.
        
        Processes a POST request containing 'usuario' and 'password' fields. If authentication is successful and the user is active, logs in the user and returns a JSON response indicating success and the username. If authentication fails or the user is inactive, returns a JSON response with an appropriate error message. All responses have HTTP status 200.
        """
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
        """
        Attempts to authenticate and log in a user without credentials via a PUT request.
        
        Returns a JSON response indicating success and the username if authentication succeeds and the user is active, or an error message otherwise. Always responds with HTTP status 200.
        """
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
    """
    Logs out the current user and redirects to the login page.
    """
    logout(request)
    return redirect('/seguridad/login/')
