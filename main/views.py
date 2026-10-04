from django.shortcuts import render
from rest_framework import viewsets

from .models import Categoria, Producto, Proveedor
from .serializers import CategoriaSerializer, ProductoSerializer, ProveedorSerializer


# ---------- Vistas HTML ----------

def home(request):
    return render(request, "home.html")


def productos(request):
    lista = Producto.objects.select_related("categoria", "proveedor")
    return render(request, "productos.html", {"productos": lista})


# ---------- API REST (CRUD) ----------

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
