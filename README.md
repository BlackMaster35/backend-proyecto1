# Proyecto Backend con Django

## Descripción
Este proyecto corresponde a la Evaluación 1 - Backend con Python y Django.  
Incluye un núcleo Django, una aplicación inicial con rutas propias, una página de bienvenida y una página personalizada de error 404.

---

## Requisitos previos
- Python 3.12 (o versión compatible)
- Git instalado
- Navegador web

---

## Instalación

1. Clonar el repositorio
   git clone https://github.com/BlackMaster35/backend-proyecto1.git
   cd backend-proyecto1

2. Crear y activar el ambiente virtual
   python -m venv .venv
   - Windows:
     .venv\Scripts\activate
   - Linux/Mac:
     source .venv/bin/activate

3. Instalar dependencias
   pip install -r requirements.txt

---

## Ejecución

1. Activar el ambiente virtual (si no está activo).
2. Ejecutar el servidor de desarrollo:
   python manage.py runserver
3. Abrir en el navegador:
   - Página principal: http://127.0.0.1:8000/ → muestra la bienvenida.
   - Página inexistente: http://127.0.0.1:8000/noexiste → muestra el 404 personalizado.

---

## Estructura del proyecto
- core/ → configuración principal del proyecto Django.
- inicio/ → aplicación inicial con vistas y rutas propias.
- templates/ → contiene 404.html.
- manage.py → archivo de gestión del proyecto.
- requirements.txt → dependencias del proyecto.
- .gitignore → exclusión de .venv, db.sqlite3 y archivos sensibles.
- README.md → instrucciones de instalación y ejecución.

---

## Autor
Proyecto desarrollado por Seba para la Evaluación 1 de Backend con Python y Django.
