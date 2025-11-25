from django.db import models
from django.utils import timezone

class Proyecto(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Título")
    descripcion = models.TextField(verbose_name="Descripción")
    imagen = models.ImageField(upload_to='proyectos/', verbose_name="Imagen")
    link_repo = models.URLField(blank=True, null=True, verbose_name="Enlace GitHub")
    link_demo = models.URLField(blank=True, null=True, verbose_name="Enlace Demo/Web")
    tecnologias = models.CharField(max_length=200, verbose_name="Tecnologías (separadas por coma)")
    
    # 2. CAMPO NUEVO (Editable manualmente)
    fecha_desarrollo = models.DateField(
        verbose_name="Fecha de Realización", 
        default=timezone.now
    )
    
    # orden interno
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de subida")

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        # Ordena el más nuevo primero
        ordering = ['-fecha_desarrollo'] 

    def __str__(self):
        return self.titulo
    
    def lista_tecnologias(self):
        return self.tecnologias.split(',')

class CarouselItem(models.Model):
    title = models.CharField(max_length=100, verbose_name="Título Principal")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(upload_to='carousel/', verbose_name="Imagen de Fondo") # Obligatoria ahora
    
    button_text = models.CharField(max_length=50, default="Ver más", verbose_name="Texto del Botón")
    button_link = models.CharField(max_length=200, default="#proyectos", verbose_name="Enlace")
    order = models.IntegerField(default=0, verbose_name="Orden")

    class Meta:
        verbose_name = "Slide del Carrusel"
        verbose_name_plural = "Slides del Carrusel"
        ordering = ['order']

    def __str__(self):
        return self.title
    
class Skill(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre Habilidad")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Habilidad"
        verbose_name_plural = "Habilidades"
        ordering = ['created']

    def __str__(self):
        return self.name
    
    
class Mensaje(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    email = models.EmailField(verbose_name="Correo")
    contenido = models.TextField(verbose_name="Mensaje")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de envío")

    class Meta:
        verbose_name = "Mensaje de Contacto"
        verbose_name_plural = "Mensajes de Contacto"
        ordering = ['-created_at'] # Los más recientes primero

    def __str__(self):
        return f"Mensaje de {self.nombre}"