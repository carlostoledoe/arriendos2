from main.models import Comuna, Inmueble, UserProfile
from django.contrib.auth.models import User
from django.db.utils import IntegrityError


def crear_inmueble(nombre:str, descripcion:str, m2_construidos:int, m2_totales:int, num_estacionamientos:int, num_habitaciones:int, num_baños:int, direccion:str, precio_mensual_arriendo:int, tipo_de_inmueble:str, comuna_cod:str, rut_propietario:str):
    comuna = Comuna.objects.get(cod=comuna_cod)
    propietario = User.objects.get(username=rut_propietario)
    Inmueble.objects.create(
        nombre = nombre,
        descripcion = descripcion,
        m2_construidos = m2_construidos,
        m2_totales = m2_totales,
        num_estacionamientos = num_estacionamientos,
        num_habitaciones = num_habitaciones,
        num_baños = num_baños,
        direccion = direccion,
        precio_mensual_arriendo = precio_mensual_arriendo,
        tipo_de_inmueble = tipo_de_inmueble,
        comuna = comuna,
        propietario = propietario,
    )
    return True


def crear_user(username:str, first_name:str, last_name:str, email:str, password:str, pass_confirm:str, direccion:str, rol:str='arrendatario', telefono:str=None) -> bool:
    if password != pass_confirm:
        # messages.error(request, 'Las contraseñas no coinciden')
        return False
    try:
        user = User.objects.create_user(
            username,
            email,
            password,
            first_name=first_name,
            last_name=last_name,
        )
    except IntegrityError:
        # messages.error(request, 'El rut ya está ingresado')
        return False
    UserProfile.objects.create(
        direccion=direccion,
        telefono_personal=telefono,
        rol = rol,
        user=user
    )
    # messages.success(request, 'Usuario creado con éxito! Por favor, ingrese')
    return True