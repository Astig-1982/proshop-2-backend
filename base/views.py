from django.shortcuts import render
from django.http import JsonResponse #JsonResponse will render on the server the output of the view. This is instead of using html files to render the output
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .products import products #we import products list from products.py file
from .models import Product
from .serializers import ProductSerializer

# Create your views here.

@api_view(['GET']) # in the parantheses we pass the methods we want to allow for this view: GET, POST, DELETE, PUT
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
    return Response(routes)
    ## return JsonResponse(routes, safe=False) -- the JsonResponse return if we are not using api views


@api_view(['GET'])
def allProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProduct(request, id): 
    # the pk is being sent by the url in urls.py. It is passed in the url.py by the API call in the frontend: fetch(`/api/products/${this.props.match.params.id}`). This fetch call matches the url path in urls.py
    product = get_object_or_404(Product, pk=id)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)

"""
Below is the response we are getting from the above api view:

[
    {
        "_id": "1",
        "name": "Airpods Wireless Bluetooth Headphones",
        "image": "/images/airpods.jpg",
        "description": "Bluetooth technology lets you connect it with compatible devices wirelessly High-quality AAC audio offers immersive listening experience Built-in microphone allows you to take calls while working",
        "brand": "Apple",
        "category": "Electronics",
        "price": 89.99,
        "countInStock": 10,
        "rating": 4.5,
        "numReviews": 12
    },
    {
        "_id": "2",
        "name": "iPhone 11 Pro 256GB Memory",
        "image": "/images/phone.jpg",
        "description": "Introducing the iPhone 11 Pro. A transformative triple-camera system that adds tons of capability without complexity. An unprecedented leap in battery life",
        "brand": "Apple",
        "category": "Electronics",
        "price": 599.99,
        "countInStock": 0,
        "rating": 4.0,
        "numReviews": 8
    },
    ...
"""

"""
def allProducts(request):
    return JsonResponse(products, safe=False)

Below is the response we are getting with the above normal view with JsonResponse:

[{"_id": "1", "name": "Airpods Wireless Bluetooth Headphones", "image": "/images/airpods.jpg", "description": "Bluetooth technology lets you connect it with compatible devices wirelessly High-quality AAC audio offers immersive listening experience Built-in microphone allows you to take calls while working", "brand": "Apple", "category": "Electronics", "price": 89.99, "countInStock": 10, "rating": 4.5, "numReviews": 12}, {"_id": "2", "name": "iPhone 11 Pro 256GB Memory", "image": "/images/phone.jpg", "description": "Introducing the iPhone 11 Pro. A transformative triple-camera system that adds tons of capability without complexity. An unprecedented leap in battery life", "brand": "Apple", "category": "Electronics", "price": 599.99, "countInStock": 0, "rating": 4.0, "numReviews": 8}, {"_id": "3", "name": "Cannon EOS 80D DSLR Camera", "image": "/images/camera.jpg", "description": "Characterized by versatile imaging specs, the Canon EOS 80D further clarifies itself using a pair of robust focusing systems and an intuitive design", "brand": "Cannon", "category": "Electronics", "price": 929.99, "countInStock": 5, "rating": 3, "numReviews": 12}, {"_id": "4", "name": "Sony Playstation 4 Pro White Version", "image": "/images/playstation.jpg", "description": "The ultimate home entertainment center starts with PlayStation. Whether you are into gaming, HD movies, television, music", "brand": "Sony", "category": "Electronics", "price": 399.99, "countInStock": 11, "rating": 5, "numReviews": 12}, {"_id": "5", "name": "Logitech G-Series Gaming Mouse", "image": "/images/mouse.jpg", "description": "Get a better handle on your games with this Logitech LIGHTSYNC gaming mouse. The six programmable buttons allow customization for a smooth playing experience", "brand": "Logitech", "category": "Electronics", "price": 49.99, "countInStock": 7, "rating": 3.5, "numReviews": 10}, {"_id": "6", "name": "Amazon Echo Dot 3rd Generation", "image": "/images/alexa.jpg", "description": "Meet Echo Dot - Our most popular smart speaker with a fabric design. It is our most compact smart speaker that fits perfectly into small space", "brand": "Amazon", "category": "Electronics", "price": 29.99, "countInStock": 2, "rating": 4, "numReviews": 12}]
"""
    
    
    
