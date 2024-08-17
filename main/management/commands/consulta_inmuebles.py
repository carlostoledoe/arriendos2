import csv
from django.core.management.base import BaseCommand
from main.services import obtener_propiedades_comunas

# Este código crea un archivo de text si hay inmuebles que tiene en su nombre o en su descripción el filtro que se agrega
# Uso: si quiero conocer inmuebles que contienen en su nombre o descripción el filtro, se consulta así:
# En el terminal:
# python manage.py consulta_inmuebles -f playa  
# python manage.py consulta_inmuebles  

class Command(BaseCommand):
    def add_arguments(self, parser):
        # Posicional arguments
        parser.add_argument('-f', '--f', type=str, nargs='+')
    
    def handle(self, *args, **kwargs):
        filtro = None
        if 'f' in kwargs.keys() and kwargs['f'] is not None:
            filtro = kwargs['f'][0]
        inmuebles = obtener_propiedades_comunas(filtro)
        
        with open('data/inmuebles_comuna.txt', 'w') as file:
            for inmueble in inmuebles:
                linea = f'{inmueble.nombre}\t{inmueble.descripcion}\t\t{inmueble.comuna.nombre}\n'
                file.write(linea)