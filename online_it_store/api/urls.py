from django.urls import path
from .views import ProductListAPIView, ProductDetailAPIView, CategoryListAPIView, OrderListAPIView
from .views import search

urlpatterns = [
    path('api/', ProductListAPIView.as_view()),
    path('api/<int:pk>/', ProductDetailAPIView.as_view()),
    path('categories/', CategoryListAPIView.as_view()),
    path('orders/', OrderListAPIView.as_view()),
    path('search/', search, name='search'),
]
