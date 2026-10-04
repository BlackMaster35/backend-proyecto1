from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Hotel(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True)
    estrellas = models.PositiveSmallIntegerField(
        default=3, validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    class Meta:
        verbose_name = "Hotel"
        verbose_name_plural = "Hoteles"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class TipoHabitacion(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True)
    capacidad = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])
    precio_noche = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Tipo de habitación"
        verbose_name_plural = "Tipos de habitación"
        ordering = ["precio_noche"]

    def __str__(self):
        return self.nombre


class Habitacion(models.Model):
    ESTADOS = [
        ("disponible", "Disponible"),
        ("ocupada", "Ocupada"),
        ("mantencion", "En mantención"),
    ]

    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="habitaciones")
    tipo = models.ForeignKey(TipoHabitacion, on_delete=models.PROTECT, related_name="habitaciones")
    numero = models.CharField(max_length=10)
    piso = models.PositiveSmallIntegerField(default=1)
    estado = models.CharField(max_length=15, choices=ESTADOS, default="disponible")

    class Meta:
        verbose_name = "Habitación"
        verbose_name_plural = "Habitaciones"
        ordering = ["hotel", "numero"]
        constraints = [
            models.UniqueConstraint(fields=["hotel", "numero"], name="habitacion_unica_por_hotel")
        ]

    def __str__(self):
        return f"{self.hotel} - Hab. {self.numero}"


class Huesped(models.Model):
    rut = models.CharField(max_length=12, unique=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Huésped"
        verbose_name_plural = "Huéspedes"
        ordering = ["apellidos", "nombres"]

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"


class Recepcionista(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.PROTECT, related_name="recepcionistas")
    rut = models.CharField(max_length=12, unique=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Recepcionista"
        verbose_name_plural = "Recepcionistas"
        ordering = ["apellidos", "nombres"]

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"


class Reserva(models.Model):
    ESTADOS = [
        ("pendiente", "Pendiente"),
        ("confirmada", "Confirmada"),
        ("checkin", "Check-in"),
        ("checkout", "Check-out"),
        ("cancelada", "Cancelada"),
    ]

    huesped = models.ForeignKey(Huesped, on_delete=models.PROTECT, related_name="reservas")
    habitacion = models.ForeignKey(Habitacion, on_delete=models.PROTECT, related_name="reservas")
    recepcionista = models.ForeignKey(
        Recepcionista, on_delete=models.SET_NULL, null=True, blank=True, related_name="reservas"
    )
    fecha_entrada = models.DateField()
    fecha_salida = models.DateField()
    cantidad_huespedes = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1)])
    estado = models.CharField(max_length=15, choices=ESTADOS, default="pendiente")
    total = models.PositiveIntegerField(default=0)
    creada_en = models.DateTimeField(auto_now_add=True)
    actualizada_en = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"
        ordering = ["-fecha_entrada"]

    def clean(self):
        if self.fecha_entrada and self.fecha_salida and self.fecha_salida <= self.fecha_entrada:
            raise ValidationError("La fecha de salida debe ser posterior a la fecha de entrada.")

    def __str__(self):
        return f"Reserva #{self.pk} - {self.huesped}"


class Pago(models.Model):
    METODOS = [
        ("efectivo", "Efectivo"),
        ("debito", "Débito"),
        ("credito", "Crédito"),
        ("transferencia", "Transferencia"),
    ]

    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE, related_name="pagos")
    monto = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    metodo = models.CharField(max_length=15, choices=METODOS)
    fecha_pago = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Pago"
        verbose_name_plural = "Pagos"
        ordering = ["-fecha_pago"]

    def __str__(self):
        return f"Pago #{self.pk} - {self.monto}"
