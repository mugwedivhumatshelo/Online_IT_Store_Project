from django.contrib import admin
from django.urls import path, include
from .views import index, about, contact, product_detail, search_results
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('api.urls')),  # Include the API URLs from the api app
    path('', index, name='index'),  # Add this line for the root URL
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('search/', search_results, name='search_results'),
    path('categories/', include('categories.urls')),
    path('orders/', include('orders.urls')),
    path('users/', include('users.urls')),
    path('product/<pk>/', product_detail, name='product_detail'),
] 
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

