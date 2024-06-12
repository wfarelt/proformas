from django.urls import path
from .views import home, proformas_list, productos_list, proforma_new, proforma_edit,\
    agregar_producto_a_detalle, producto_new, eliminar_producto_a_detalle, \
        clientes_list, cliente_new, cliente_edit, cliente_delete, \
            product_detail, product_edit

urlpatterns = [
    path('', home, name='home'),
    #productos
    path('producto/<int:id>/', product_detail, name='product_detail'),
    path('producto/new/', producto_new, name='producto_new'),
    path('producto/edit/<int:id>/', product_edit, name='product_edit'),
    path('productos/', productos_list, name='productos_list'),
    #proformas
    path('proformas/', proformas_list, name='proformas_list'),
    path('proforma/new/', proforma_new, name='proforma_new'),
    path('proforma/edit/<int:id>/', proforma_edit, name='proforma_edit'),
    path('proforma/agregar_producto_a_detalle/', agregar_producto_a_detalle, name='agregar_producto_a_detalle'),
    path('proforma/eliminar_producto_a_detalle/<int:id>/', eliminar_producto_a_detalle, name='eliminar_producto_a_detalle'),
    #clientes
    path('clientes/', clientes_list, name='clientes_list'),
    path('cliente/new/', cliente_new, name='cliente_new'),
    path('cliente/edit/<int:id>/', cliente_edit, name='cliente_edit'),
    path('cliente/delete/<int:id>/', cliente_delete, name='cliente_delete'),
]
