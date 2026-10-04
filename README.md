# Sistema de Hotel — API REST con Django + Django REST Framework

**Proyecto 26: Sistema de Hotel** — Evaluación 2, Programación Backend (INACAP 2026).

API REST que digitaliza la gestión de reservas hoteleras: hoteles, habitaciones,
huéspedes, recepcionistas, reservas y pagos, con CRUD completo
(`GET`, `POST`, `PUT`, `PATCH`, `DELETE`).

## Modelo de datos
| Modelo | Campos principales | Relaciones |
|--------|--------------------|------------|
| **Hotel** | nombre, direccion, ciudad, telefono, estrellas (1-5) | — |
| **TipoHabitacion** | nombre, descripcion, capacidad, precio_noche | — |
| **Habitacion** | numero, piso, estado (disponible / ocupada / mantencion) | FK → Hotel, FK → TipoHabitacion |
| **Huesped** | rut, nombres, apellidos, email, telefono, fecha_registro | — |
| **Recepcionista** | rut, nombres, apellidos, email, activo | FK → Hotel |
| **Reserva** | fecha_entrada, fecha_salida, cantidad_huespedes, estado, total | FK → Huesped, Habitacion, Recepcionista |
| **Pago** | monto, metodo, fecha_pago | FK → Reserva |

Reglas de negocio:
- Un número de habitación no se repite dentro del mismo hotel.
- La fecha de salida de una reserva debe ser posterior a la de entrada.
- Estados de reserva: pendiente → confirmada → check-in → check-out (o cancelada).

## Instalación
```bash
git clone https://github.com/BlackMaster35/backend-proyecto1.git
cd backend-proyecto1
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # Linux/Mac
pip install -r requirements.txt
copy .env.example .env          # Windows (luego editar los valores)
# cp .env.example .env          # Linux/Mac
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Base de datos
El script `sql/script_bd.sql` (MySQL) crea:
1. La base de datos `sistema_hotel`.
2. El usuario `hotel_user`.
3. Los permisos de ese usuario sobre esa base.
4. Las tablas del modelo de datos.

## Variables de entorno
Los datos sensibles (`SECRET_KEY`, `DEBUG`, conexión a la base de datos) se leen
desde el archivo `.env` con `python-dotenv`. Ese archivo **no se sube** al repositorio
(está en `.gitignore`); se incluye `.env.example` como plantilla.

## Endpoints
| URL | Descripción |
|-----|-------------|
| `/` | Página de inicio |
| `/admin/` | Panel de administración |
| `/api/` | Raíz de la API |
| `/api/hoteles/` | CRUD de hoteles |
| `/api/tipos-habitacion/` | CRUD de tipos de habitación |
| `/api/habitaciones/` | CRUD de habitaciones |
| `/api/huespedes/` | CRUD de huéspedes |
| `/api/recepcionistas/` | CRUD de recepcionistas |
| `/api/reservas/` | CRUD de reservas |
| `/api/pagos/` | CRUD de pagos |

En `/api/<recurso>/`: `GET` (listar) y `POST` (crear).
En `/api/<recurso>/<id>/`: `GET` (detalle), `PUT` / `PATCH` (actualizar) y `DELETE` (eliminar).

## Estructura
```
core/          configuración del proyecto (settings, urls)
hotel/         app: models, admin, serializers, views (ModelViewSet), urls (Router)
sql/           script SQL de base de datos, usuario y permisos
.env.example   plantilla de variables de entorno
requirements.txt
```

## Autor
Sebastián Valderrama Concha — INACAP, Analista Programador.
