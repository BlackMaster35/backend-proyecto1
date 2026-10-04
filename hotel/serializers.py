from rest_framework import serializers

from .models import Habitacion, Hotel, Huesped, Pago, Recepcionista, Reserva, TipoHabitacion


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = "__all__"


class TipoHabitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoHabitacion
        fields = "__all__"


class HabitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habitacion
        fields = "__all__"


class HuespedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Huesped
        fields = "__all__"


class RecepcionistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recepcionista
        fields = "__all__"


class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = "__all__"

    def validate(self, data):
        entrada = data.get("fecha_entrada", getattr(self.instance, "fecha_entrada", None))
        salida = data.get("fecha_salida", getattr(self.instance, "fecha_salida", None))
        if entrada and salida and salida <= entrada:
            raise serializers.ValidationError(
                "La fecha de salida debe ser posterior a la fecha de entrada."
            )
        return data


class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = "__all__"
