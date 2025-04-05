from django.contrib import admin
from django.urls import path
from django.urls import include, path
from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('api.urls')),  # Include the API URLs from the api app
    path('', index),  # Add this line for the root URL
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
]
