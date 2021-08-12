from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name='routes'),
    path('products', views.allProducts, name='products'),
    path('products/<pk>/', views.getProduct, name='product'),
]