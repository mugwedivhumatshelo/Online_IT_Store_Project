from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Product, Category, Order, User
from django.db.models import Q
from .serializers import ProductSerializer, CategorySerializer, OrderSerializer

class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class OrderListAPIView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class SearchAPIView(APIView):
    def get(self, request):
        query = request.GET.get('q')
        if query:
            categories = Category.objects.filter(Q(name__icontains=query))
            products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
            orders = Order.objects.filter(Q(user__username__icontains=query))
            users = User.objects.filter(Q(username__icontains=query) | Q(email__icontains=query))
            data = {
                'categories': CategorySerializer(categories, many=True).data,
                'products': ProductSerializer(products, many=True).data,
                'orders': OrderSerializer(orders, many=True).data,
                'users': UserSerializer(users, many=True).data,
            }
            return Response(data)
        else:
            return Response({
                'categories': [],
                'products': [],
                'orders': [],
                'users': [],
            })
