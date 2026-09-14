from django.contrib import admin
from django.urls import path
from inicio.views import bienvenida

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bienvenida),  # Página principal
]
