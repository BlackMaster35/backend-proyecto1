from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

from hotel import views

urlpatterns = [
    path("admin/", admin.site.urls),

    # Vista pública
    path("", views.home, name="home"),

    # Autenticación (vistas nativas de Django)
    path("login/", auth_views.LoginView.as_view(
        template_name="registration/login.html",
        redirect_authenticated_user=True,
    ), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),

    # Vistas privadas basadas en funciones (@login_required)
    path("dashboard/", views.dashboard, name="dashboard"),
    path("reservas/", views.lista_reservas, name="lista_reservas"),
    path("reservas/<int:pk>/", views.detalle_reserva, name="detalle_reserva"),

    # Vistas privadas basadas en clases (LoginRequiredMixin)
    path("perfil/", views.PerfilView.as_view(), name="perfil"),
    path("habitaciones/", views.HabitacionListView.as_view(), name="lista_habitaciones"),
    path("habitaciones/<int:pk>/", views.HabitacionDetailView.as_view(), name="detalle_habitacion"),
    path("huespedes/", views.HuespedListView.as_view(), name="lista_huespedes"),

    # API REST (requiere autenticación)
    path("api/", include("hotel.urls")),
]
