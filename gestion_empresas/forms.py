from django import forms
from .models import Empresa, Estado

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        # Aquí incluimos los campos que coinciden con tu imagen y modelo
        fields = [
            'nombre_empresa', 
            'fecha_inicio', 
            'fecha_finalizacion', 
            'telefono', 
            'correo_electronico', 
            'responsable', 
            'estado'
        ]
        # Añadimos widgets para que los campos de fecha se vean como calendarios
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'fecha_finalizacion': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'nombre_empresa': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre empresa'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número de teléfono'}),
            'correo_electronico': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ejemplo@correo.com'}),
            'responsable': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del encargado'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
        }