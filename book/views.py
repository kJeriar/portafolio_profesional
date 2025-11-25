from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Proyecto, CarouselItem, Skill, Mensaje

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

# --- VISTA NUEVA: DETALLE DEL PROYECTO (SINGLE) ---
def proyecto_detalle(request, proyecto_id):
    # Busca el proyecto o lanza error 404 si no existe
    proyecto = get_object_or_404(Proyecto, pk=proyecto_id)
    return render(request, 'proyecto_detalle.html', {'proyecto': proyecto})