from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator

class User(AbstractUser):
    email = models.EmailField(unique=True)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='api_user_set',
        related_query_name='api_user',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='api_user_permission_set',
        related_query_name='api_user_permission',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    description = models.TextField()

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey('api.User', on_delete=models.CASCADE, related_name='api_orders')
    product = models.ForeignKey('api.Product', on_delete=models.CASCADE, related_name='api_product_orders', null=True, blank=True)
    quantity = models.IntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"
