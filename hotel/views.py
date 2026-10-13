from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView, TemplateView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

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


# =====================================================================
# VISTA PÚBLICA (única vista sin autenticación)
# =====================================================================

def home(request):
    """Página de bienvenida. Es la única vista pública del sistema."""
    return render(request, "home.html")


# =====================================================================
# VISTAS PRIVADAS BASADAS EN FUNCIONES (FBV) -> decorador @login_required
# Si el usuario no ha iniciado sesión, Django lo redirige a /login/?next=...
# =====================================================================

@login_required
def dashboard(request):
    """Panel principal con el resumen del hotel."""
    contexto = {
        "total_hoteles": Hotel.objects.count(),
        "total_habitaciones": Habitacion.objects.count(),
        "habitaciones_disponibles": Habitacion.objects.filter(estado="disponible").count(),
        "total_huespedes": Huesped.objects.count(),
        "total_reservas": Reserva.objects.count(),
        "reservas_pendientes": Reserva.objects.filter(estado="pendiente").count(),
        "ultimas_reservas": Reserva.objects.select_related("huesped", "habitacion")[:5],
    }
    return render(request, "dashboard.html", contexto)


@login_required
def lista_reservas(request):
    """Listado de reservas (FBV protegida)."""
    reservas = Reserva.objects.select_related("huesped", "habitacion", "habitacion__hotel")
    return render(request, "reservas/lista.html", {"reservas": reservas})


@login_required
def detalle_reserva(request, pk):
    """Detalle de una reserva con sus pagos (FBV protegida)."""
    reserva = get_object_or_404(Reserva, pk=pk)
    return render(request, "reservas/detalle.html", {"reserva": reserva})


# =====================================================================
# VISTAS PRIVADAS BASADAS EN CLASES (CBV) -> LoginRequiredMixin
# El mixin va SIEMPRE a la izquierda de la vista genérica.
# =====================================================================

class PerfilView(LoginRequiredMixin, TemplateView):
    """Datos del usuario que inició sesión."""
    template_name = "perfil.html"


class HabitacionListView(LoginRequiredMixin, ListView):
    """Listado de habitaciones."""
    model = Habitacion
    template_name = "habitaciones/lista.html"
    context_object_name = "habitaciones"

    def get_queryset(self):
        return Habitacion.objects.select_related("hotel", "tipo")


class HabitacionDetailView(LoginRequiredMixin, DetailView):
    """Detalle de una habitación."""
    model = Habitacion
    template_name = "habitaciones/detalle.html"
    context_object_name = "habitacion"


class HuespedListView(LoginRequiredMixin, ListView):
    """Listado de huéspedes."""
    model = Huesped
    template_name = "huespedes/lista.html"
    context_object_name = "huespedes"


# =====================================================================
# API REST (CRUD con ModelViewSet) -> permiso IsAuthenticated
# Sin sesión iniciada la API responde 403 Forbidden.
# =====================================================================

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [IsAuthenticated]


class TipoHabitacionViewSet(viewsets.ModelViewSet):
    queryset = TipoHabitacion.objects.all()
    serializer_class = TipoHabitacionSerializer
    permission_classes = [IsAuthenticated]


class HabitacionViewSet(viewsets.ModelViewSet):
    queryset = Habitacion.objects.all()
    serializer_class = HabitacionSerializer
    permission_classes = [IsAuthenticated]


class HuespedViewSet(viewsets.ModelViewSet):
    queryset = Huesped.objects.all()
    serializer_class = HuespedSerializer
    permission_classes = [IsAuthenticated]


class RecepcionistaViewSet(viewsets.ModelViewSet):
    queryset = Recepcionista.objects.all()
    serializer_class = RecepcionistaSerializer
    permission_classes = [IsAuthenticated]


class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
    permission_classes = [IsAuthenticated]


class PagoViewSet(viewsets.ModelViewSet):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer
    permission_classes = [IsAuthenticated]
