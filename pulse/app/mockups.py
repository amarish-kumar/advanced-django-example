from django.core.management.base import NoArgsCommand, make_option

from models import Enlace, Categoria
from django.contrib.auth.models import User

class EnlaceMockup():
    def __init__(self, instances = 0 ):
        self.instances = instances
        setUp()

    def setUp(self):
        self.categoria = Categoria.objects.create(titulo='Categoria de prueba')
        self.usuario = User.objects.create_user(username='pepe', password='barbas')

    def run():
        for i in range(self.instances):
            enlace = Enlace.objects.create(titulo='Enlace de prueba %d' % i, enlace='http://www.google.com', votos=0, categoria=self.categoria, usuario=self.usuario)
            enlace.save()
