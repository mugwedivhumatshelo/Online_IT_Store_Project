from django.shortcuts import render
from django.http import HttpResponse
from api.models import Product

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def search_results(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        if query:
            results = Product.objects.filter(name__icontains=query)
            return render(request, 'search_results.html', {'results': results, 'query': query})
        else:
            return render(request, 'search_results.html', {'results': None, 'query': None})
    else:
        return HttpResponse("Invalid request method")

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'product_detail.html', {'product': product})
