from django.urls import path
from .views import CategoryListAPIView, CategoryDetailAPIView

urlpatterns = [
    path('', CategoryListAPIView.as_view()),
    path('<int:pk>/', CategoryDetailAPIView.as_view()),
]
