from django.shortcuts import render, redirect
from main.services import crear_user, editar_user_sin_password, cambio_password
from django.contrib.auth.decorators import login_required
from main.models import Inmueble
from django.contrib import messages

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
    


@login_required
def profile(request):
    id_usuario = request.user.id
    propiedades = Inmueble.objects.filter(propietario_id=id_usuario)
    context = {
        'propiedades': propiedades
    }

    if request.method == 'POST':
        if request.POST['telefono'].strip() != '':
            username = request.user
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            direccion = request.POST['direccion']
            telefono = request.POST['telefono']
            rol = request.POST['rol']
            editar_user_sin_password(username, first_name, last_name, email, direccion, rol, telefono)
            messages.success(request, 'Ha actualizado sus datos con exito')
            return redirect('/accounts/profile')
        else:
            username = request.user
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            direccion = request.POST['direccion']
            rol = request.POST['rol']
                        
            editar_user_sin_password(username, first_name, last_name, email, rol, direccion)
            messages.success(request, 'Ha actualizado sus datos con exito sin telefono')
            return redirect('/accounts/profile')
    else:
        return render(request, 'profile.html', context)

def change_pass(request):
    password = request.POST['password']
    password_repeat = request.POST['password_repeat']
    cambio_password(request, password, password_repeat)
    return redirect('/accounts/profile')