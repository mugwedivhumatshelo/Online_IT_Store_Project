from django.urls import path
from .views import UserView, UserDetailView
from . import views

urlpatterns = [
    path('users/', UserView.as_view()),
    path('users/<int:pk>/', UserDetailView.as_view()),
    path('products/', views.ProductListView.as_view()),
    path('products/<int:pk>/', views.ProductDetailView.as_view()),
    path('products/create/', views.ProductCreateView.as_view()),
    path('products/<int:pk>/update/', views.ProductUpdateView.as_view()),
    path('products/<int:pk>/delete/', views.ProductDeleteView.as_view()),
    path('services/', views.ServiceListView.as_view()),
    path('services/<int:pk>/', views.ServiceDetailView.as_view()),
    path('services/create/', views.ServiceCreateView.as_view()),
    path('services/<int:pk>/update/', views.ServiceUpdateView.as_view()),
    path('services/<int:pk>/delete/', views.ServiceDeleteView.as_view()),
    path('cart/', views.CartView.as_view()),
    path('cart/<int:pk>/', views.CartDetailView.as_view()),
    path('orders/', views.OrderView.as_view()),
    path('orders/<int:pk>/', views.OrderDetailView.as_view()),
]
