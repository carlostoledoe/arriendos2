from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        print('Este es en ejemplo. Hola Mundo!!')