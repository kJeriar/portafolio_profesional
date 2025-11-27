from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from .models import Proyecto, CarouselItem, Skill, Mensaje, Curriculum, Perfil, Tecnologia
import os
from django.http import FileResponse, Http404
from django.conf import settings

def home(request):
    # --- POST  ---
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        contenido = request.POST.get('contenido')  # 👈 IGUAL QUE EL name DEL TEXTAREA

        # Validación básica
        if nombre and email and contenido:
            Mensaje.objects.create(
                nombre=nombre,
                email=email,
                contenido=contenido       # 👈 coincide con tu modelo
            )
            messages.success(request, 'Mensaje enviado con éxito')
        else:
            messages.error(request, 'Todos los campos son obligatorios')

        return redirect('home')

    # --- GET  ---
    todos_proyectos = Proyecto.objects.all().order_by('-created')
    proyectos_home = todos_proyectos[:8]
    hay_mas_proyectos = todos_proyectos.count() > 8

    slides = CarouselItem.objects.all().order_by('order')
    skills = Skill.objects.all()
    
    return render(request, 'index.html', {
        'proyectos': proyectos_home,
        'hay_mas_proyectos': hay_mas_proyectos, 
        'slides': slides,
        'skills': skills
    })
    
# --- DETALLE DEL PROYECTO (SINGLE) ---
def proyecto_detalle(request, proyecto_id):
    # Busca el proyecto o lanza error 404 si no existe
    proyecto = get_object_or_404(Proyecto, pk=proyecto_id)
    return render(request, 'proyecto_detalle.html', {'proyecto': proyecto})

# def lista_proyectos(request):
#     # Traemos TODOS los proyectos, ordenados por fecha
#     proyectos = Proyecto.objects.all().order_by('-fecha_desarrollo')
#     return render(request, 'lista_proyectos.html', {'proyectos': proyectos})

def lista_proyectos(request):
    # 1. Traer TODAS las tecnologías para el dropdown del formulario
    todas_tecnologias = Tecnologia.objects.all().order_by('nombre')

    # 2. Capturar el filtro de la URL
    tecnologia_filtrar = request.GET.get('tec')
    
    # 3. Inicialmente, traemos todos los proyectos
    proyectos = Proyecto.objects.all().order_by('-fecha_desarrollo') 
    
    if tecnologia_filtrar:

        proyectos = proyectos.filter(
            tecnologias__nombre__iexact=tecnologia_filtrar 
        )
        
        
    return render(request, 'lista_proyectos.html', {
        'proyectos': proyectos,
        'tecnologias': todas_tecnologias, 
        'tecnologia_activa': tecnologia_filtrar 
    })

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