from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('proyecto/<int:proyecto_id>/', views.proyecto_detalle, name='proyecto_detalle'),
    path('proyectos/', views.lista_proyectos, name='lista_proyectos'),
    path('sobre-mi/', views.about, name='about'),
    path('descargar-cv/', views.descargar_cv, name='descargar_cv'),
]