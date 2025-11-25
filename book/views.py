from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Proyecto, CarouselItem, Skill, Mensaje, Curriculum, Perfil
import os
from django.http import FileResponse, Http404
from django.conf import settings

def home(request):
    # --- POST (Formulario) ---
    if request.method == 'POST':
        # ... (Mantén tu lógica de formulario aquí igual que antes) ...
        nombre = request.POST.get('nombre')
        # ... etc ...
        messages.success(request, 'Mensaje enviado')
        return redirect('home')

    # --- GET (Carga de datos) ---
    
    # 1. Traer TODOS los proyectos ordenados
    todos_proyectos = Proyecto.objects.all().order_by('-created')
    
    # 2. Cortar la lista: Solo los primeros 8 para el Home
    proyectos_home = todos_proyectos[:8]
    
    # 3. ¿Hay más de 8? (Para saber si mostramos el botón "Ver todos")
    hay_mas_proyectos = todos_proyectos.count() > 8

    slides = CarouselItem.objects.all().order_by('order')
    skills = Skill.objects.all()
    
    return render(request, 'index.html', {
        'proyectos': proyectos_home,       # Enviamos solo 8
        'hay_mas_proyectos': hay_mas_proyectos, # Enviamos el "chivato" booleano
        'slides': slides,
        'skills': skills
    })

# --- DETALLE DEL PROYECTO (SINGLE) ---
def proyecto_detalle(request, proyecto_id):
    # Busca el proyecto o lanza error 404 si no existe
    proyecto = get_object_or_404(Proyecto, pk=proyecto_id)
    return render(request, 'proyecto_detalle.html', {'proyecto': proyecto})

def lista_proyectos(request):
    # Traemos TODOS los proyectos, ordenados por fecha
    proyectos = Proyecto.objects.all().order_by('-fecha_desarrollo')
    return render(request, 'lista_proyectos.html', {'proyectos': proyectos})

def about(request):
    return render(request, 'about.html')


def descargar_cv(request):
    if request.method == 'POST':
        codigo_ingresado = request.POST.get('codigo')
        
        # Buscamos en la BD: ¿Existe algún CV con esta clave?
        # .filter(...).first() devuelve el objeto o None si no existe
        cv_encontrado = Curriculum.objects.filter(codigo_acceso=codigo_ingresado).first()
        
        if cv_encontrado:
            # ¡Clave correcta! Iniciamos la descarga
            # Usamos el nombre original del archivo para la descarga
            return FileResponse(
                cv_encontrado.archivo.open('rb'), 
                as_attachment=True, 
                filename=f"CV_Karla_{cv_encontrado.nombre}.pdf"
            )
        else:
            # Clave no encontrada en la base de datos
            messages.error(request, 'Código incorrecto o expirado. Inténtalo de nuevo.')

    return render(request, 'acceso_cv.html')

def about(request):
    # Intentamos obtener el perfil (o None si aún no creas la entrada)
    try:
        perfil = Perfil.objects.get(pk=1)
    except Perfil.DoesNotExist:
        perfil = None 
        
    return render(request, 'about.html', {'perfil': perfil})