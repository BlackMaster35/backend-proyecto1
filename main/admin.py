from django.contrib import admin

from .models import Categoria, Producto, Proveedor


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "descripcion")
    search_fields = ("nombre",)


@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "rut", "telefono", "email")
    search_fields = ("nombre", "rut")


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "precio", "stock", "categoria", "proveedor")
    list_filter = ("categoria", "proveedor")
    search_fields = ("nombre",)
