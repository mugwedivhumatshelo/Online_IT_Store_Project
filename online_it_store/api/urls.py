from django.urls import path
from .views import UserView, UserDetailView
from . import views

urlpatterns = [
    path('users/', UserView.as_view()),
    path('users/<int:pk>/', UserDetailView.as_view()),
    path('products/', views.ProductListView.as_view()),
    path('services/', views.ServiceListView.as_view()),
    path('products/<int:pk>/', views.ProductDetailView.as_view()),
    path('services/<int:pk>/', views.ServiceDetailView.as_view()),
    path('cart/', views.CartView.as_view()),
    path('cart/<int:pk>/', views.CartDetailView.as_view()),
]

