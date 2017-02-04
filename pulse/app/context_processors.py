from random import choice
from django.urls import reverse
from django.core.cache import cache

frases = ['I have to learn advanced Django', 'Also, I have to practice English', 'But I am hungry right now']

def ejemplo(request):
    frase = cache.get('frase_cool')

    if frase is None:
        frase = choice(frases)
        cache.set('frase_cool', frase)

    return {'frase' : frase}

def menu(request):
    menu = {'menu' : [
        {'name': 'Home', 'url': reverse('home')},
        {'name': 'Add', 'url': reverse('add')},
        {'name': 'Acerca de...', 'url': reverse('about')},
    ]}

    for item in menu['menu']:
        if request.path == item['url']:
            item['active'] = True
    return menu
