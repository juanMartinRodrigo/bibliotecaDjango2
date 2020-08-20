from django.contrib import admin
from App.models import *

class MaterialInline(admin.TabularInline):
    model = TMaterial

class RevistaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'numero','status',]
    inlines = [MaterialInline, ]

class LibroAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'status', 'editorial',]
    inlines = [MaterialInline, ]

class PersonaInline(admin.TabularInline):
    model = TPersona

class AlumnoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'matricula', 'NumLibros', 'adeudo',]
    inlines = [PersonaInline,]

class ProfesorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'adeudo', 'NumLibros', 'numEmpleado',]
    inlines = [PersonaInline,]

class PrestamoAdmin(admin.ModelAdmin):
    list_display = ['persona', 'material', 'fechaSalida', 'fechaRegreso']


# Register your models here.

admin.site.register(Libro, LibroAdmin)
admin.site.register(Revista, RevistaAdmin)
admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(Profesor,ProfesorAdmin)
admin.site.register(Prestamo, PrestamoAdmin)