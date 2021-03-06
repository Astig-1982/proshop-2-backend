from django.db import models
from django.contrib.auth.models import User # we are importing the defalult User model from Django. Just we we did in Solid Properties and created LandlordProfile. 
"""
We are importing the defalult User model from Django, just we we did in Solid Properties and created LandlordProfile.
In Solid Properties we have connected LandlordProfile model to OneToOneField (given by Django) to User model 
"""

# Create your models here.

class Product(models.Model):
    """
    basically this model is connected to a ForeignKey to User model, as the users can created different products in the logic of this project.
    """
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) # on_delete=SET_NULL will not delete the product if the user that is connected to gets deleted
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=True, blank=True) # install 'pillow' in order ImageField to work
    brand = models.CharField(max_length=200, null=True, blank=True)
    category = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    rating = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    numReviews = models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    countInStock = models.IntegerField(null=True, blank=True, default=0)
    createdAt = models.DateTimeField(auto_now_add=True) # this takes a snapshot of when the product has been created
    _id = models.AutoField(primary_key=True, editable=False) # this will override the default primary key by django and will set up '_id' filed as a primary key. we have done this because when
                                                             # we created products.js, each product has _id key and we don't want to modify the frontend now

    def __str__(self):
        return self.name ## this function will return the name of the product in the admin panel


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    rating = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True) # models.IntegerField(null=True, blank=True, default=0)
    comment = models.TextField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.rating) # this stringify the rating which is a decimal


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    paymentMethod = models.CharField(max_length=200, null=True, blank=True) # Stripe, PayPal
    taxPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    shippingPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    totalPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    isPaid = models.DateTimeField(auto_now_add=True)
    paidAt = models.DateTimeField(auto_now_add=True)
    isDelivered = models.BooleanField(default=False)
    deliveredAt = models.DateTimeField(auto_now_add=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.createdAt)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True) # on_delete=models.SET_NULL will NOT delete the item if the product with the primary key is deleted
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True) # on_delete=models.CASCADE will delete the item if the order with the primary key is deleted
    name = models.CharField(max_length=200, null=True, blank=True)
    qty = models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    image = models.CharField(max_length=200, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.name


class ShippingAddress(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    postalCode = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    shippingPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.address


