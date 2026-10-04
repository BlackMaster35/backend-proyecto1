from django.contrib import admin
from django.urls import include, path

from main import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("productos/", views.productos, name="productos"),
    path("api/", include("main.urls")),
]
