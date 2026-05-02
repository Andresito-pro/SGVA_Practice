from django.db import models

# Tabla de estados (el catálogo que mencionaste)
class Estado(models.Model):
    nombre_estado = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_estado

# Tabla principal de Empresas
class Empresa(models.Model):
    nombre_empresa = models.CharField(max_length=100)
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_finalizacion = models.DateField(null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    correo_electronico = models.EmailField(null=True, blank=True)
    responsable = models.CharField(max_length=100, null=True, blank=True)
    # Relación con la tabla de estados (Llave foránea)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_empresa