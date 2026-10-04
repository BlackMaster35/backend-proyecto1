from rest_framework.routers import DefaultRouter

from .views import (
    HabitacionViewSet,
    HotelViewSet,
    HuespedViewSet,
    PagoViewSet,
    RecepcionistaViewSet,
    ReservaViewSet,
    TipoHabitacionViewSet,
)

router = DefaultRouter()
router.register(r"hoteles", HotelViewSet)
router.register(r"tipos-habitacion", TipoHabitacionViewSet)
router.register(r"habitaciones", HabitacionViewSet)
router.register(r"huespedes", HuespedViewSet)
router.register(r"recepcionistas", RecepcionistaViewSet)
router.register(r"reservas", ReservaViewSet)
router.register(r"pagos", PagoViewSet)

urlpatterns = router.urls
