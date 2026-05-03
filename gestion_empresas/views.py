from django.shortcuts import render, redirect
from .forms import EmpresaForm
from .models import Empresa, Estado  # <--- ¡Faltaba importar los modelos!

def gestor_empresas(request):
    if request.method == 'POST':
        # Usamos el método manual ya que tu HTML tiene los 'name' personalizados
        nombre = request.POST.get('empresa')
        f_inicio = request.POST.get('fecha_inicio')
        f_fin = request.POST.get('fecha_fin')
        tel = request.POST.get('telefono')
        mail = request.POST.get('correo')
        resp = request.POST.get('responsable')
        estado_id = request.POST.get('estado')

        try:
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
        except Estado.DoesNotExist:
            # Si el ID del estado no existe, podrías manejar el error aquí
            pass

        return redirect('index')

    # Si es GET, consultamos todas las empresas
    empresas = Empresa.objects.all().select_related('estado')
    return render(request, 'index.html', {'empresas': empresas})


from django.shortcuts import get_object_or_404

def eliminar_empresa(request, id):
    empresa = get_object_or_404(Empresa, id=id)
    empresa.delete()
    return redirect('index')