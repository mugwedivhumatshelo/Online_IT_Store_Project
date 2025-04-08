from django.urls import path
from .views import ProductListAPIView, ProductDetailAPIView, CategoryListAPIView, OrderListAPIView, SearchAPIView

urlpatterns = [
    path('', ProductListAPIView.as_view()),
    path('<int:pk>/', ProductDetailAPIView.as_view()),
    path('categories/', CategoryListAPIView.as_view()),
    path('orders/', OrderListAPIView.as_view()),
    path('search/', SearchAPIView.as_view(), name='search'),
]
