from django.contrib import admin
from .models import Producto, Proforma, Detalle
# Import Export
from import_export.resources import ModelResource
from import_export.admin import ImportExportModelAdmin


# Register your models here.


admin.site.register(Proforma)

admin.site.register(Detalle)

# Import Export Productos
class ProductoResource(ModelResource):
    class Meta:
        model = Producto


@admin.register(Producto)
class ProductoAdmin(ImportExportModelAdmin):
    resource_class = ProductoResource        