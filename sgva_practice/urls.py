from django.contrib import admin
from django.urls import path
from gestion_empresas.views import gestor_empresas # Importamos tu vista

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', gestor_empresas, name='index'), # La página principal
]

# Importa la nueva vista primero
from gestion_empresas.views import gestor_empresas, eliminar_empresa

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', gestor_empresas, name='index'),
    path('eliminar/<int:id>/', eliminar_empresa, name='eliminar_empresa'), # Nueva ruta
]