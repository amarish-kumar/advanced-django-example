from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    titulo = models.CharField(max_length = 140)

    def __unicode__(self):
        return self.titulo


class Enlace(models.Model):
    titulo = models.CharField(max_length = 140)
    enlace = models.URLField()
    votos = models.IntegerField(default=0)
    categoria = models.ForeignKey(Categoria)
    usuario = models.ForeignKey(User)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "%s - %s" % (self.titulo,self.enlace)

    def mis_votos_en_imagen_rosada(self):
        return 'http://placehold.it/200x100/E8117F/ffffff/&text=%d+votos' % self.votos

    def es_popular(self):
        return self.votos > 5

    # Server crash
    # es_popular.boolean = True

class Agregador(models.Model):
    titulo = models.CharField(max_length = 140)
    enlaces = models.ManyToManyField(Enlace)

    def __unicode__(self):
        return self.titulo

# For clear cache when anyone object is inserted
from django.core.cache import cache
from django.db.models.signals import post_save
from django.contrib.sessions.models import Session
from django.dispatch import receiver

@receiver(post_save)
def clear_cache(sender, **kwargs):
    if sender != Session:
	cache.clear()
