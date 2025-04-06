from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

class Category(models.Model):
    name = models.CharField(max_length=255)

class Order(models.Model):
    user = models.ForeignKey('api.User', on_delete=models.CASCADE, related_name='api_orders')
    product = models.ForeignKey('api.Product', on_delete=models.CASCADE, related_name='api_product_orders', null=True, blank=True)
    quantity = models.IntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
