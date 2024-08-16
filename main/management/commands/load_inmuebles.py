import csv
from django.core.management.base import BaseCommand
from main.models import Comuna
from main.services import crear_inmueble

# Se ejecuta usando python manage.py test_client

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        archivo = open('data/inmuebles.csv', 'r')
        reader = csv.reader(archivo, delimiter=',')
        next(reader) # Se salta la primera linea
        for fila in reader:
            crear_inmueble(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6], fila[7], fila[8], fila[9], fila[10], fila[11])
