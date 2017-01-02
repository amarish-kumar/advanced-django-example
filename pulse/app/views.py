from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context
from django.template.loader import get_template
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required

from datetime import datetime
from models import Categoria, Enlace
from forms import EnlaceForm

# Create your views here.

def home(request):
    categorias = Categoria.objects.all()
    enlaces = Enlace.objects.order_by('-votos').all()
    template = "index.html"
    return render_to_response(template, locals())

def categoria(request, categoria_id):
    categorias = Categoria.objects.all()
    cat = get_object_or_404(Categoria, pk = categoria_id)
    enlaces = Enlace.objects.filter(categoria = cat)
    template = "index.html"
    return render_to_response(template, locals())

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
        form = EnlaceForm(request.POST)
        if form.is_valid():
            enlace = form.save(commit = False)
            enlace.usuario = request.user
            enlace.save()

            return HttpResponseRedirect("/app/")
    else:
        form = EnlaceForm()

    template = "form.html"

    ##########################
    # DEPRECATED in Django 1.8################################################################
    # return render_to_response(template, context_instance = RequestContext(request,locals()))
    ##########################################################################################

    return render(request, template, locals())
