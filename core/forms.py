
from django import forms
from .models import Producto, Cliente

# CREAR UN FORMULARIO PARA PRODUCTO
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'stock', 'precio']
        labels = {
            'nombre': 'Nombre',
            'descripcion': 'Descripción',
            'stock': 'Stock',
            'precio': 'Precio',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}), # 'type': 'number
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),            
        }

# CREAR UN FORMULARIO PARA CLIENTE
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['name', 'nit', 'email', 'phone', 'address']
        labels = {
            'name': 'Nombre',
            'nit': 'NIT',
            'email': 'Correo',
            'phone': 'Teléfono',
            'address': 'Dirección',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'nit': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
        }