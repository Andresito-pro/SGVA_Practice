from django.contrib import admin
from django.urls import path
from gestion_empresas.views import gestor_empresas # Importamos tu vista

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', gestor_empresas, name='index'), # La página principal
]