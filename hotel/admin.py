from django.contrib import admin

from .models import Habitacion, Hotel, Huesped, Pago, Recepcionista, Reserva, TipoHabitacion


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "ciudad", "estrellas", "telefono")
    search_fields = ("nombre", "ciudad")


@admin.register(TipoHabitacion)
class TipoHabitacionAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "capacidad", "precio_noche")


@admin.register(Habitacion)
class HabitacionAdmin(admin.ModelAdmin):
    list_display = ("id", "hotel", "numero", "piso", "tipo", "estado")
    list_filter = ("hotel", "tipo", "estado")
    search_fields = ("numero",)


@admin.register(Huesped)
class HuespedAdmin(admin.ModelAdmin):
    list_display = ("id", "rut", "nombres", "apellidos", "email", "telefono")
    search_fields = ("rut", "nombres", "apellidos", "email")


@admin.register(Recepcionista)
class RecepcionistaAdmin(admin.ModelAdmin):
    list_display = ("id", "rut", "nombres", "apellidos", "hotel", "activo")
    list_filter = ("hotel", "activo")


@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ("id", "huesped", "habitacion", "fecha_entrada", "fecha_salida", "estado", "total")
    list_filter = ("estado", "habitacion__hotel")
    search_fields = ("huesped__nombres", "huesped__apellidos", "huesped__rut")


@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ("id", "reserva", "monto", "metodo", "fecha_pago")
    list_filter = ("metodo",)
