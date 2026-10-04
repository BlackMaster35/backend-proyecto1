from django.shortcuts import render
from rest_framework import viewsets

from .models import Habitacion, Hotel, Huesped, Pago, Recepcionista, Reserva, TipoHabitacion
from .serializers import (
    HabitacionSerializer,
    HotelSerializer,
    HuespedSerializer,
    PagoSerializer,
    RecepcionistaSerializer,
    ReservaSerializer,
    TipoHabitacionSerializer,
)


# ---------- Vista HTML ----------

def home(request):
    return render(request, "home.html")


# ---------- API REST (CRUD con ModelViewSet) ----------

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class TipoHabitacionViewSet(viewsets.ModelViewSet):
    queryset = TipoHabitacion.objects.all()
    serializer_class = TipoHabitacionSerializer


class HabitacionViewSet(viewsets.ModelViewSet):
    queryset = Habitacion.objects.all()
    serializer_class = HabitacionSerializer


class HuespedViewSet(viewsets.ModelViewSet):
    queryset = Huesped.objects.all()
    serializer_class = HuespedSerializer


class RecepcionistaViewSet(viewsets.ModelViewSet):
    queryset = Recepcionista.objects.all()
    serializer_class = RecepcionistaSerializer


class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer


class PagoViewSet(viewsets.ModelViewSet):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer
