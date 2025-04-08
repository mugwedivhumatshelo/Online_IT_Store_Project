from django.urls import path
from .views import OrderListAPIView, OrderDetailAPIView

urlpatterns = [
    path('', OrderListAPIView.as_view()),
    path('<int:pk>/', OrderDetailAPIView.as_view()),
]
