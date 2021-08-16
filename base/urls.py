from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name='routes'),
    path('products', views.allProducts, name='products'),
    path('products/<id>/', views.getProduct, name='product'),
]