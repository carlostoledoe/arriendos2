from django.shortcuts import render, redirect
from main.services import crear_user

# Create your views here.
def index(request):
    return render(request, 'index.html',)

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        direccion = request.POST['direccion']
        telefono = request.POST['telefono']
        rol = request.POST['rol']
        password = request.POST['password']
        password_repeat = request.POST['password_repeat']
            
        crear = crear_user(request, username, first_name, last_name, email, password, password_repeat, direccion, rol, telefono)

        if crear: # Si crear es True
            return redirect('/accounts/login') 
        # Si llegó, crear fue False
        return render(request, 'registration/register.html', {
            'username': username,
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'direccion': direccion,
            'telefono': telefono,
            'rol': rol,
            })
    else: # en caso de metodo GET
        return render(request, 'registration/register.html')