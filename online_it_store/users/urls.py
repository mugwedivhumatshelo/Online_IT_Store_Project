from django.urls import path
from .views import UserListAPIView, UserDetailAPIView

urlpatterns = [
    path('users/', UserListAPIView.as_view()),
    path('users/<int:pk>/', UserDetailAPIView.as_view()),
]

