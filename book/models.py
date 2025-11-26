from django.db import models
from django.utils import timezone

# =====================================================
# 1. MODELOS AUXILIARES (Para relaciones)
# =====================================================

class Tecnologia(models.Model):
    """Para relación Muchos a Muchos con Proyecto"""
    nombre = models.CharField(max_length=50, unique=True, verbose_name="Nombre de Tecnología")
    
    def __str__(self):
        return self.nombre

# =====================================================
# 2. MODELOS PRINCIPALES
# =====================================================

class Proyecto(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Título")
    descripcion = models.TextField(verbose_name="Descripción")
    imagen = models.ImageField(upload_to='proyectos/', verbose_name="Imagen")
    link_repo = models.URLField(blank=True, null=True, verbose_name="Enlace GitHub")
    link_demo = models.URLField(blank=True, null=True, verbose_name="Enlace Demo/Web")
    
    # RELACIÓN MUCHOS A MUCHOS (M:M)
    # Cumple requerimiento: "entidades con relaciones muchos a muchos"
    tecnologias = models.ManyToManyField(Tecnologia, verbose_name="Tecnologías usadas")
    
    fecha_desarrollo = models.DateField(
        verbose_name="Fecha de Realización", 
        default=timezone.now
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de subida")

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        ordering = ['-fecha_desarrollo'] 

    def __str__(self):
        return self.titulo

class CarouselItem(models.Model):
    title = models.CharField(max_length=100, verbose_name="Título Principal")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(upload_to='carousel/', verbose_name="Imagen de Fondo")
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
    """Habilidades generales para la sección 'Sobre mí'"""
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
        ordering = ['-created_at']

    def __str__(self):
        return f"Mensaje de {self.nombre}"

class Curriculum(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre interno (ej: CV Python)")
    codigo_acceso = models.CharField(max_length=7, unique=True, verbose_name="Clave de Seguridad")
    archivo = models.FileField(upload_to='cvs/', verbose_name="Archivo PDF")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Curriculum Protegido"
        verbose_name_plural = "Curriculums Protegidos"

    def __str__(self):
        return f"{self.nombre} (Clave: {self.codigo_acceso})"

# =====================================================
# 3. PERFIL Y RELACIONADOS (1:1 y 1:M)
# =====================================================

class Perfil(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Título Principal")
    subtitulo = models.CharField(max_length=150, verbose_name="Subtítulo")
    foto = models.ImageField(upload_to='perfil/', verbose_name="Foto de Perfil", blank=True, null=True)
    bio_parrafo1 = models.TextField(verbose_name="Párrafo 1 (Mi Enfoque)")
    bio_parrafo2 = models.TextField(verbose_name="Párrafo 2 (Experiencia)", blank=True, null=True)
    bio_parrafo3 = models.TextField(verbose_name="Párrafo 3 (Compromiso)", blank=True, null=True)
    
    class Meta:
        verbose_name = "Perfil Personal"
        verbose_name_plural = "Perfil Personal"
    
    def __str__(self):
        return self.titulo
    
    def save(self, *args, **kwargs):
        if Perfil.objects.exists() and not self.pk:
            pass
        super(Perfil, self).save(*args, **kwargs)

class ExperienciaLaboral(models.Model):
    # RELACIÓN UNO A MUCHOS (1:M)
    # Cumple requerimiento: "entidades con relaciones uno a muchos"
    perfil = models.ForeignKey(
        'Perfil',
        on_delete=models.CASCADE,
        related_name='experiencias',
        verbose_name="Perfil asociado"
    )
    titulo = models.CharField(max_length=150, verbose_name="Título del Cargo")
    empresa = models.CharField(max_length=100, verbose_name="Empresa")
    descripcion = models.TextField(verbose_name="Descripción")
    fecha_inicio = models.DateField(default=timezone.now, verbose_name="Fecha de Inicio")
    fecha_fin = models.DateField(null=True, blank=True, verbose_name="Fecha de Fin")
    
    class Meta:
        verbose_name = "Experiencia Laboral"
        verbose_name_plural = "Experiencia Laboral"
        ordering = ['-fecha_inicio']

    def __str__(self):
        return f"{self.titulo} en {self.empresa}"

class Certificacion(models.Model):
    # RELACIÓN UNO A UNO (1:1)
    perfil = models.OneToOneField(
        'Perfil',  # <--- OJO AQUÍ: Debe ser 'Perfil' (con comillas y Mayúscula)
        on_delete=models.CASCADE,
        verbose_name="Perfil Asociado"
    )
    nombre = models.CharField(max_length=100, verbose_name="Nombre Certificación")
    institucion = models.CharField(max_length=100, verbose_name="Institución")
    fecha_obtencion = models.DateField(default=timezone.now)

    class Meta:
        verbose_name = "Certificación Destacada"
        verbose_name_plural = "Certificaciones"

    def __str__(self):
        return self.nombre