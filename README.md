# Sistema de Hotel â€” API REST con Django + Django REST Framework

**Proyecto 26: Sistema de Hotel** â€” EvaluaciÃ³n 3, ProgramaciÃ³n Backend (INACAP 2026).

API REST que digitaliza la gestiÃ³n de reservas hoteleras: hoteles, habitaciones,
huÃ©spedes, recepcionistas, reservas y pagos, con CRUD completo
(`GET`, `POST`, `PUT`, `PATCH`, `DELETE`), mÃ¡s autenticaciÃ³n de usuarios y
control de acceso entre vistas pÃºblicas y privadas.

## Modelo de datos
| Modelo | Campos principales | Relaciones |
|--------|--------------------|------------|
| **Hotel** | nombre, direccion, ciudad, telefono, estrellas (1-5) | â€” |
| **TipoHabitacion** | nombre, descripcion, capacidad, precio_noche | â€” |
| **Habitacion** | numero, piso, estado (disponible / ocupada / mantencion) | FK â†’ Hotel, FK â†’ TipoHabitacion |
| **Huesped** | rut, nombres, apellidos, email, telefono, fecha_registro | â€” |
| **Recepcionista** | rut, nombres, apellidos, email, activo | FK â†’ Hotel |
| **Reserva** | fecha_entrada, fecha_salida, cantidad_huespedes, estado, total | FK â†’ Huesped, Habitacion, Recepcionista |
| **Pago** | monto, metodo, fecha_pago | FK â†’ Reserva |

Reglas de negocio:
- Un nÃºmero de habitaciÃ³n no se repite dentro del mismo hotel.
- La fecha de salida de una reserva debe ser posterior a la de entrada.
- Estados de reserva: pendiente â†’ confirmada â†’ check-in â†’ check-out (o cancelada).

## InstalaciÃ³n
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

## Base de datos (MySQL)
Scripts en `sql/`, ejecutar en orden como `root`:

| Script | QuÃ© hace |
|--------|----------|
| `01_crear_base_datos.sql` | Crea la base `sistema_hotel` (utf8mb4) |
| `02_crear_usuario.sql` | Crea el usuario de aplicaciÃ³n `hotel_user` |
| `03_asignar_permisos.sql` | Da a `hotel_user` permisos solo sobre `sistema_hotel` |

```bash
mysql -u root -p < sql/01_crear_base_datos.sql
mysql -u root -p < sql/02_crear_usuario.sql
mysql -u root -p < sql/03_asignar_permisos.sql
python manage.py migrate
```

## Variables de entorno
Los datos sensibles (`SECRET_KEY`, `DEBUG`, conexiÃ³n a la base de datos) se leen
desde el archivo `.env` con `python-dotenv`. Ese archivo **no se sube** al repositorio
(estÃ¡ en `.gitignore`); se incluye `.env.example` como plantilla.

## AutenticaciÃ³n y control de acceso
Se usa el sistema de autenticaciÃ³n nativo de Django (`django.contrib.auth`).

| URL | Vista | Tipo | Acceso |
|-----|-------|------|--------|
| `/` | `home` | FBV | **PÃºblica** (Ãºnica vista pÃºblica) |
| `/login/` | `LoginView` | CBV nativa | Formulario de inicio de sesiÃ³n |
| `/logout/` | `LogoutView` | CBV nativa | Cierra sesiÃ³n (por `POST`, botÃ³n del menÃº) |
| `/dashboard/` | `dashboard` | FBV + `@login_required` | Privada |
| `/reservas/` | `lista_reservas` | FBV + `@login_required` | Privada |
| `/reservas/<id>/` | `detalle_reserva` | FBV + `@login_required` | Privada |
| `/perfil/` | `PerfilView` | CBV (`TemplateView`) + `LoginRequiredMixin` | Privada |
| `/habitaciones/` | `HabitacionListView` | CBV (`ListView`) + `LoginRequiredMixin` | Privada |
| `/habitaciones/<id>/` | `HabitacionDetailView` | CBV (`DetailView`) + `LoginRequiredMixin` | Privada |
| `/huespedes/` | `HuespedListView` | CBV (`ListView`) + `LoginRequiredMixin` | Privada |
| `/api/...` | `ModelViewSet` | DRF + `IsAuthenticated` | Privada |

Comportamiento:
- Usuario **no autenticado** en una vista HTML privada â†’ `302` a `/login/?next=<ruta>` con mensaje de acceso denegado.
- Usuario **no autenticado** en la API â†’ `403 Forbidden` (JSON).
- Login correcto â†’ `302` a `/dashboard/` (`LOGIN_REDIRECT_URL`).
- Logout â†’ `302` a `/` (`LOGOUT_REDIRECT_URL`).

Crear un usuario para iniciar sesiÃ³n:
```bash
python manage.py createsuperuser
```

## Endpoints de la API
| URL | DescripciÃ³n |
|-----|-------------|
| `/api/` | RaÃ­z de la API |
| `/api/hoteles/` | CRUD de hoteles |
| `/api/tipos-habitacion/` | CRUD de tipos de habitaciÃ³n |
| `/api/habitaciones/` | CRUD de habitaciones |
| `/api/huespedes/` | CRUD de huÃ©spedes |
| `/api/recepcionistas/` | CRUD de recepcionistas |
| `/api/reservas/` | CRUD de reservas |
| `/api/pagos/` | CRUD de pagos |

En `/api/<recurso>/`: `GET` (listar) y `POST` (crear).
En `/api/<recurso>/<id>/`: `GET` (detalle), `PUT` / `PATCH` (actualizar) y `DELETE` (eliminar).
Todos requieren sesiÃ³n iniciada (o Basic Auth).

## Estructura
```
core/          configuraciÃ³n del proyecto (settings, urls)
hotel/         app: models, admin, serializers, views (FBV, CBV y ModelViewSet), urls (Router)
hotel/templates/  base, home, login, dashboard, perfil, reservas, habitaciones, huespedes
sql/           scripts SQL: base de datos, usuario y permisos
.env.example   plantilla de variables de entorno
requirements.txt
```

## Autor
SebastiÃ¡n Valderrama Concha â€” INACAP, Analista Programador.
