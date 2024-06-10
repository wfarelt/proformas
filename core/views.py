from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import Proforma, Producto, Detalle
from .forms import ProductoForm

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

#añadir form a mi vista producto_new
def producto_new(request):
    form = ProductoForm()
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('productos_list')
    context = {'form': form}
    return render(request, 'core/producto_new.html', context)    

def proformas_list(request):
    proformas = Proforma.objects.all()
    context = {'proformas': proformas}
    return render(request, 'core/proformas_list.html', context)

def productos_list(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, 'core/productos_list.html', context)

def proforma_new(request):
    proforma = Proforma.objects.create()
    productos_list = Producto.objects.all()
    context = {'proforma': proforma, 'productos_list': productos_list}
    return render(request, 'core/proforma_new.html', context)

def proforma_edit(request, id):
    proforma = Proforma.objects.get(id=id)
    detalles = Detalle.productos_list(proforma)
    productos_list = Producto.objects.all()
    context = {'proforma': proforma, 'productos_list': productos_list, 'detalles': detalles}
    return render(request, 'core/proforma_new.html', context)

def agregar_producto_a_detalle(request):
    # VALIR DATOS SI ES POST O GET
    if request.method == 'POST':
        proforma_id = request.POST.get('proforma_id')
        producto_id = request.POST.get('producto_id')
        cantidad = request.POST.get('cantidad')  
        #añadir a subtotal en float
        subtotal =  request.POST.get('subtotal')
        # CREAR DETALLE
        #proforma = Proforma.objects.get(id=proforma_id)
        #producto = Producto.objects.get(id=producto_id)
        #detalle = Detalle.objects.create(proforma=proforma, producto=producto, cantidad=cantidad, subtotal=subtotal)
        #detalle.save()
        # ACTUALIZAR TOTAL DE PROFORMA        
        #proforma.total = proforma.total 
        #proforma.save()
        # REDIRECCIONAR A LA MISMA PAGINA
        return redirect(reverse_lazy('proforma_edit', args=[proforma_id]), subtotal=subtotal)
    else:
        return render(request, 'core/home.html')
    

    
    
    
    