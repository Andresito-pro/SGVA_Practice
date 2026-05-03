from django.contrib import admin
from .models import Estado, Empresa

@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_estado')

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nombre_empresa', 'responsable', 'estado', 'fecha_inicio')
    list_filter = ('estado',) # Esto te permite filtrar empresas por estado a la derecha
    search_fields = ('nombre_empresa', 'responsable') # Esto añade una barra de búsqueda