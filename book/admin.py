from django.contrib import admin
# AQUÍ ESTABA EL ERROR: Faltaba agregar ", Mensaje" al final
from .models import Proyecto, CarouselItem, Skill, Mensaje 

# 1. Configuración para Proyectos
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tecnologias', 'fecha_desarrollo')

# 2. Configuración para el Carrusel
class CarouselAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'button_text') 
    list_editable = ('order',) 

# 3. Configuración para Habilidades
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'created')

# 4. Configuración para Mensajes (NUEVO)
class MensajeAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'created_at')
    readonly_fields = ('created_at',)

# --- Registro de Modelos ---
admin.site.register(Proyecto, ProyectoAdmin)
admin.site.register(CarouselItem, CarouselAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Mensaje, MensajeAdmin)