from django.contrib import admin
from .models import Producto, Proforma, Detalle

# Register your models here.

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio')
    search_fields = ('nombre',)

admin.site.register(Proforma)

admin.site.register(Detalle)