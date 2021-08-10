from django.shortcuts import render
from django.http import JsonResponse #JsonResponse will render on the server the output of the view. This is instead of using html files to render the output

from .products import products #we import products list from products.py file

# Create your views here.

def getRoutes(request):
    routes = [
        '/api/products/',
        '/api/products/create/',

        '/api/products/upload/',

        '/api/products/<id>/reviews',

        '/api/products/top/',
        '/api/products/<id>',

        '/api/products/delete/<id>',
        '/api/products/<update>/<id>',
    ]
    return JsonResponse(routes, safe=False)


def allProducts(request):
    return JsonResponse(products, safe=False)

    
    
    
