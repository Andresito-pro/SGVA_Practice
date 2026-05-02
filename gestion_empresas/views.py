from django.shortcuts import render, redirect
from .models import Empresa, Estado

def gestor_empresas(request):
    if request.method == 'POST':
        # Recibimos los datos del formulario (usando los 'name' del HTML)
        nombre = request.POST.get('empresa')
        f_inicio = request.POST.get('fecha_inicio')
        f_fin = request.POST.get('fecha_fin')
        tel = request.POST.get('telefono')
        mail = request.POST.get('correo')
        resp = request.POST.get('responsable')
        estado_id = request.POST.get('estado')

        # Buscamos el objeto Estado que corresponde al ID seleccionado
        estado_obj = Estado.objects.get(id=estado_id)

        # Creamos y guardamos la nueva empresa
        Empresa.objects.create(
            nombre_empresa=nombre,
            fecha_inicio=f_inicio if f_inicio else None,
            fecha_finalizacion=f_fin if f_fin else None,
            telefono=tel,
            correo_electronico=mail,
            responsable=resp,
            estado=estado_obj
        )
        return redirect('index') # Recarga la página para ver los cambios

    # Si es GET, consultamos todas las empresas para mostrarlas en la tabla
    empresas = Empresa.objects.all().select_related('estado')
    return render(request, 'index.html', {'empresas': empresas})