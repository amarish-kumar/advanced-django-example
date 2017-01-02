from django import forms
from django.forms import ModelForm
import django

from models import Categoria, Enlace

class EnlaceForm(ModelForm):

    class Meta:
        model = Enlace
        exclude = ('votos','usuario')
