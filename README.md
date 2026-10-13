# Sistema de Hotel — API REST con Django + Django REST Framework

**Proyecto 26: Sistema de Hotel** — Evaluación 3, Programación Backend (INACAP 2026).

API REST que digitaliza la gestión de reservas hoteleras: hoteles, habitaciones,
huéspedes, recepcionistas, reservas y pagos, con CRUD completo
(`GET`, `POST`, `PUT`, `PATCH`, `DELETE`), más autenticación de usuarios y
control de acceso entre vistas públicas y privadas.

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

## Requisitos
- Python 3.10 o superior
- MySQL o MariaDB en ejecución
- Git

## Instalación (paso a paso)

### 1. Clonar el repositorio
```bash
git clone https://github.com/BlackMaster35/backend-proyecto1.git
cd backend-proyecto1
```

### 2. Crear y activar el entorno virtual
```bash
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # Linux/Mac
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno
```bash
copy .env.example .env          # Windows
# cp .env.example .env          # Linux/Mac
```
Luego editar `.env` con los valores reales (`SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS` y datos de conexión a la base de datos).

### 5. Crear base de datos, usuario y permisos (MySQL, como `root`)
```bash
mysql -u root -p < sql/01_crear_base_datos.sql
mysql -u root -p < sql/02_crear_usuario.sql
mysql -u root -p < sql/03_asignar_permisos.sql
```
> **Importante:** este paso debe hacerse **antes** de `migrate`; si no, la base `sistema_hotel` no existirá y la migración fallará.

### 6. Aplicar migraciones y crear usuario administrador
```bash
python manage.py migrate
python manage.py createsuperuser
```

### 7. Ejecutar el servidor
```bash
python manage.py runserver
```
Abrir `http://127.0.0.1:8000/` en el navegador e iniciar sesión en `/login/` con el usuario creado.

## Base de datos (MySQL)
Scripts en `sql/`, ejecutar en orden como `root`:

| Script | Qué hace |
|--------|----------|
| `01_crear_base_datos.sql` | Crea la base `sistema_hotel` (utf8mb4) |
| `02_crear_usuario.sql` | Crea el usuario de aplicación `hotel_user` |
| `03_asignar_permisos.sql` | Da a `hotel_user` permisos solo sobre `sistema_hotel` |

La aplicación se conecta con `hotel_user` (no con `root`), siguiendo el principio de mínimo privilegio.

## Variables de entorno
Los datos sensibles (`SECRET_KEY`, `DEBUG`, conexión a la base de datos) se leen
desde el archivo `.env` con `python-dotenv`. Ese archivo **no se sube** al repositorio
(está en `.gitignore`); se incluye `.env.example` como plantilla.

## Autenticación y control de acceso
Se usa el sistema de autenticación nativo de Django (`django.contrib.auth`).

| URL | Vista | Tipo | Acceso |
|-----|-------|------|--------|
| `/` | `home` | FBV | **Pública** (única vista pública) |
| `/login/` | `LoginView` | CBV nativa | Formulario de inicio de sesión |
| `/logout/` | `LogoutView` | CBV nativa | Cierra sesión (por `POST`, botón del menú) |
| `/dashboard/` | `dashboard` | FBV + `@login_required` | Privada |
| `/reservas/` | `lista_reservas` | FBV + `@login_required` | Privada |
| `/reservas/<id>/` | `detalle_reserva` | FBV + `@login_required` | Privada |
| `/perfil/` | `PerfilView` | CBV (`TemplateView`) + `LoginRequiredMixin` | Privada |
| `/habitaciones/` | `HabitacionListView` | CBV (`ListView`) + `LoginRequiredMixin` | Privada |
| `/habitaciones/<id>/` | `HabitacionDetailView` | CBV (`DetailView`) + `LoginRequiredMixin` | Privada |
| `/huespedes/` | `HuespedListView` | CBV (`ListView`) + `LoginRequiredMixin` | Privada |
| `/api/...` | `ModelViewSet` | DRF + `IsAuthenticated` | Privada |

Comportamiento:
- Usuario **no autenticado** en una vista HTML privada → `302` a `/login/?next=<ruta>` con mensaje de acceso denegado.
- Usuario **no autenticado** en la API → `403 Forbidden` (JSON).
- Login correcto → `302` a `/dashboard/` (`LOGIN_REDIRECT_URL`).
- Logout → `302` a `/` (`LOGOUT_REDIRECT_URL`).

## Endpoints de la API
| URL | Descripción |
|-----|-------------|
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
Todos requieren sesión iniciada (o Basic Auth).

## Estructura
```
core/             configuración del proyecto (settings, urls)
hotel/            app: models, admin, serializers, views (FBV, CBV y ModelViewSet), urls (Router)
hotel/templates/  base, home, login, dashboard, perfil, reservas, habitaciones, huespedes
sql/              scripts SQL: base de datos, usuario y permisos
.env.example      plantilla de variables de entorno
requirements.txt
```

## Autor
Sebastián Valderrama Concha — INACAP, Analista Programador.
