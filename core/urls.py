from django.urls import path
from .views import home, proformas_list, productos_list, proforma_new, proforma_edit,\
    agregar_producto_a_detalle, producto_new, eliminar_producto_a_detalle


urlpatterns = [
    path('', home, name='home'),
    path('producto/new/', producto_new, name='producto_new'),
    path('productos/', productos_list, name='productos_list'),
    path('proformas/', proformas_list, name='proformas_list'),
    path('proforma/new/', proforma_new, name='proforma_new'),
    path('proforma/edit/<int:id>/', proforma_edit, name='proforma_edit'),
    path('proforma/agregar_producto_a_detalle/', agregar_producto_a_detalle, name='agregar_producto_a_detalle'),
    path('proforma/eliminar_producto_a_detalle/<int:id>/', eliminar_producto_a_detalle, name='eliminar_producto_a_detalle'),
]