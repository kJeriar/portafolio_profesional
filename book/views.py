from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import FileResponse
from .models import Proyecto, Skill, Mensaje, Perfil, CarouselItem, Curriculum


def home(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        contenido = request.POST.get('contenido')

        if nombre and email and contenido:
            Mensaje.objects.create(
                nombre=nombre,
                email=email,
                contenido=contenido
            )
            messages.success(request, 'Mensaje enviado con éxito')
        else:
            messages.error(request, 'Todos los campos son obligatorios')

        return redirect('home')

    proyectos = Proyecto.objects.all().order_by('-fecha_desarrollo')[:8]
    slides = CarouselItem.objects.all().order_by('order')
    skills = Skill.objects.all()

    return render(request, 'index.html', {
        'proyectos': proyectos,
        'slides': slides,
        'skills': skills
    })


def proyecto_detalle(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, pk=proyecto_id)
    return render(request, 'proyecto_detalle.html', {'proyecto': proyecto})


def lista_proyectos(request):
    tecnologias = Skill.objects.all().order_by('name')
    tecnologia_filtrar = request.GET.get('tec')

    proyectos = Proyecto.objects.all().order_by('-fecha_desarrollo')

    if tecnologia_filtrar:
        proyectos = proyectos.filter(tecnologias__name__iexact=tecnologia_filtrar)

    return render(request, 'lista_proyectos.html', {
        'proyectos': proyectos,
        'tecnologias': tecnologias,
        'tecnologia_activa': tecnologia_filtrar
    })


def about(request):
    perfil = Perfil.objects.first()
    return render(request, 'about.html', {'perfil': perfil})


def descargar_cv(request):
    if request.method == 'POST':
        codigo_ingresado = request.POST.get('codigo')

        cv_encontrado = Curriculum.objects.filter(codigo_acceso=codigo_ingresado).first()

        if cv_encontrado:
            return FileResponse(
                cv_encontrado.archivo.open('rb'),
                as_attachment=True,
                filename=f"CV_Karla_{cv_encontrado.nombre}.pdf"
            )
        else:
            messages.error(request, 'Código incorrecto o expirado. Inténtalo de nuevo.')

    return render(request, 'acceso_cv.html')
