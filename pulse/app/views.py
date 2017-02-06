from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context
from django.template.loader import get_template
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page

from datetime import datetime
from models import Categoria, Enlace
from forms import EnlaceForm
from tasks import calculo

# Create your views here.

# @cache_page(6000)
def home(request):
    categorias = Categoria.objects.all()
    enlaces = Enlace.objects.order_by('-votos').all()
    template = "app/index.html"
    calculo.delay()
    return render(request, template, locals())

def categoria(request, categoria_id):
    categorias = Categoria.objects.all()
    cat = get_object_or_404(Categoria, pk = categoria_id)
    enlaces = Enlace.objects.filter(categoria = cat)
    template = "app/index.html"
    return render(request, template, locals())

@login_required
def minus(request, enlace_id):
    enlace = Enlace.objects.get(pk=enlace_id);
    enlace.votos = enlace.votos - 1
    enlace.save()
    return HttpResponseRedirect("/app/")

@login_required
def plus(request, enlace_id):
    enlace = Enlace.objects.get(pk=enlace_id);
    enlace.votos = enlace.votos + 1
    enlace.save()
    return HttpResponseRedirect("/app/")

@login_required
def add(request):
    if request.method == "POST":
        form = EnlaceForm(request.POST, request.FILES)
        if form.is_valid():
            enlace = form.save(commit = False)
            enlace.usuario = request.user
            enlace.save()

            return HttpResponseRedirect("/app/")
    else:
        form = EnlaceForm()

    template = "app/form.html"
    return render(request, template, locals())

from django.views.generic import ListView, DetailView

class EnlaceListView(ListView):
    model = Enlace
    context_object_name = 'enlaces'
    def get_template_names(self):
        return 'app/index.html'

class EnlaceDetailView(DetailView):
        model = Enlace
        def get_template_names(self):
            return 'app/index.html'

from .serializers import EnlaceSerializer, UserSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User

class EnlaceViewSet(viewsets.ModelViewSet):
    queryset = Enlace.objects.all()
    serializer_class = EnlaceSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
