from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product, Category, Order
from django.db.models import Q
from .serializers import ProductSerializer, CategorySerializer, OrderSerializer

class ProductListAPIView(APIView):
    def get(self, request):
        api = Product.objects.all()
        serializer = ProductSerializer(api, many=True)
        return Response(serializer.data)

class ProductDetailAPIView(APIView):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

class CategoryListAPIView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

class OrderListAPIView(APIView):
    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

def search(request):
    query = request.GET.get('q')
    if query:
        categories = Category.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        api = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        orders = Order.objects.filter(Q(customer_name__icontains=query) | Q(order_date__icontains=query))
        users = User.objects.filter(Q(username__icontains=query) | Q(email__icontains=query))
        return render(request, 'search_results.html', {
            'categories': categories,
            'api': api,
            'orders': orders,
            'users': users,
        })
    else:
        return render(request, 'search_results.html', {
            'categories': [],
            'api': [],
            'orders': [],
            'users': [],
        })
