# Proyecto Backend con Django + Django REST Framework

Evaluación 2 - Backend con Python y Django. API REST con CRUD completo para
**Categorías**, **Proveedores** y **Productos**.

## Modelo de datos
- **Categoria**: nombre, descripcion
- **Proveedor**: nombre, rut, telefono, email
- **Producto**: nombre, precio, stock, categoria (FK → Categoria), proveedor (FK → Proveedor)

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

## Variables de entorno
Los datos sensibles (`SECRET_KEY`, `DEBUG`, credenciales de base de datos) se leen
desde el archivo `.env` con `python-dotenv`. Ese archivo **no se sube** al repositorio
(está en `.gitignore`); se incluye `.env.example` como plantilla.

## URLs
| URL | Descripción |
|-----|-------------|
| `/` | Página de inicio |
| `/productos/` | Lista de productos (HTML) |
| `/admin/` | Panel de administración |
| `/api/` | Raíz de la API (DRF) |
| `/api/categorias/` | CRUD de categorías |
| `/api/proveedores/` | CRUD de proveedores |
| `/api/productos/` | CRUD de productos |

Cada recurso acepta `GET` (listar), `POST` (crear) y, en `/api/<recurso>/<id>/`,
`GET` (detalle), `PUT`/`PATCH` (actualizar) y `DELETE` (eliminar).

## Estructura
- `core/` → configuración del proyecto (settings, urls).
- `main/` → app con modelos, admin, serializers, viewsets, router y templates.
- `requirements.txt` → dependencias.
- `.gitignore` → excluye `.venv`, `db.sqlite3` y cachés.

## Autor
Sebastián Valderrama — INACAP, Analista Programador.
