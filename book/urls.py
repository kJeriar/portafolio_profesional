from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # Nueva ruta para ver un proyecto solo (por su ID)
    path('proyecto/<int:proyecto_id>/', views.proyecto_detalle, name='proyecto_detalle'),
]