from django.contrib import admin
from .models import (
    Perfil,
    ExperienciaLaboral,
    Proyecto,
    CarouselItem,
    Skill,
    Mensaje,
    Curriculum,
)


class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'mostrar_tecnologias', 'fecha_desarrollo')
    list_filter = ('tecnologias',)
    filter_horizontal = ('tecnologias',)

    def mostrar_tecnologias(self, obj):
        return ", ".join([t.name for t in obj.tecnologias.all()])

    mostrar_tecnologias.short_description = "Tecnologías"


class CarouselAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'button_text')
    list_editable = ('order',)


class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'created')


class MensajeAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'created_at')
    readonly_fields = ('created_at',)


class CurriculumAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'codigo_acceso', 'created')
    search_fields = ('nombre', 'codigo_acceso')


admin.site.register(Proyecto, ProyectoAdmin)
admin.site.register(CarouselItem, CarouselAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Mensaje, MensajeAdmin)
admin.site.register(Perfil)
admin.site.register(Curriculum, CurriculumAdmin)
admin.site.register(ExperienciaLaboral)
