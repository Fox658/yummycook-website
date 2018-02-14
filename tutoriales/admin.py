from django.contrib import admin

# Register your models here.
from .models import Platos, ExperienciaEstudiante, SerieTutoriales, Leccion

class PlatosAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    list_display = ('nombre','activo',)
admin.site.register(Platos, PlatosAdmin)

admin.site.register(ExperienciaEstudiante)

class SerieTutotialesAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    list_display = ('nombre','archivado',)

admin.site.register(SerieTutoriales,SerieTutotialesAdmin)

class LeccionAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    list_display = ('titulo', 'activo', 'free_preview',)
admin.site.register(Leccion, LeccionAdmin)