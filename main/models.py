from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

# Create your models here.
class UserProfile(models.Model):
    roles = (
        ('arrendatario', 'Arrendatario'),
        ('arrendador', 'Arrendador')
    )
    direccion = models.CharField(max_length=255)
    telefono_personal = models.CharField(max_length=20, null=True)
    rol = models.CharField(max_length=50, default='arrendatario', choices=roles)
    user = models.OneToOneField(
        User,
        related_name='userprofile',
        on_delete=models.CASCADE
    )
    def __str__(self):
        nombre = self.user.first_name
        apellido = self.user.last_name
        usuario = self.user.username
        rol = self.rol
        return f'{nombre} {apellido} | {usuario} | {rol}'


class Region(models.Model):
    cod = models.CharField(max_length=5, primary_key=True)
    nombre = models.CharField(max_length=255)

class Comuna(models.Model):
    cod = models.CharField(max_length=5, primary_key=True)
    nombre = models.CharField(max_length=255)
    region = models.ForeignKey(
        Region,
        on_delete=models.RESTRICT,
        related_name='comunas'
    )
    def __str__(self):
        nombre = self.nombre
        codigo = self.cod
        return f'{nombre} | {codigo}'

class Inmueble(models.Model):
    inmuebles = (
        ('casa', 'Casa'),
        ('departamento', 'Departamento'),
        ('parcela', 'Parcela')
    )
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=1500)
    m2_construidos = models.IntegerField(validators=[MinValueValidator(1)])
    m2_totales = models.IntegerField(validators=[MinValueValidator(1)]) 
    num_estacionamientos = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    num_habitaciones = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    num_baños = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    direccion = models.CharField(max_length=255)
    precio_mensual_arriendo = models.IntegerField(validators=[MinValueValidator(1000)])
    tipo_de_inmueble = models.CharField(max_length=20, choices=inmuebles)
    comuna = models.ForeignKey(
        Comuna,
        related_name='inmuebles',
        on_delete=models.RESTRICT
    )
    propietario = models.ForeignKey(
        User,
        related_name='inmueble',
        on_delete=models.RESTRICT
    )
    def __str__(self):
        nombre = self.nombre
        comuna = self.comuna
        tipo_inmueble = self.tipo_de_inmueble
        return f'{nombre} {comuna} | {tipo_inmueble}'
