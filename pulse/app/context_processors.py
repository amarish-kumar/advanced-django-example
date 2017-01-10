from random import choice
from django.urls import reverse

frases = ['I have to learn advanced Django', 'Also, I have to practice English', 'But I am hungry right now']

def ejemplo(request):
    return {'frase': choice(frases)}

def menu(request):
    menu = {'menu' : [
        {'name': 'Home', 'url': reverse('home')},
        {'name': 'Add', 'url': reverse('add')},
    ]}

    for item in menu['menu']:
        if request.path == item['url']:
            item['active'] = True
    return menu
