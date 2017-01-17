from django.shortcuts import redirect
from random import choice

paises = ['Colombia', 'Peru', 'Cuba', 'Panama', 'Mexico']

def de_donde_vengo(request):
    return choice(paises)

class PaisMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        pais = de_donde_vengo(request)

        # if pais == 'Mexico':
        #    return redirect('http://www.google.com')

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
