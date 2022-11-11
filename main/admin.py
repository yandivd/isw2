from django.contrib import admin
from .models import *

class SexoAdmin(admin.ModelAdmin):
    list_display=('sexo',)

class EspecialidadAdmin(admin.ModelAdmin):
    list_display=('nombre',)

class MedicoAdmin(admin.ModelAdmin):
    list_display=('usuario','especialidad')

class EnfermeroAdmin(admin.ModelAdmin):
    list_display=('usuario',)

class PacienteAdmin(admin.ModelAdmin):
    list_display=('nombre','apellidos','direccion','provincia','municipio','telf_movil')

class HCAdmin(admin.ModelAdmin):
    list_display=('numero','paciente')

class EstadoAdmin(admin.ModelAdmin):
    list_display=('nombre',)

# Register your models here.
admin.site.register(Sexo, SexoAdmin)
admin.site.register(Especialidad, EspecialidadAdmin)
admin.site.register(Medico, MedicoAdmin)
admin.site.register(Enfermero, EnfermeroAdmin)
admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Historia_clinica, HCAdmin)
admin.site.register(Estado,EstadoAdmin)