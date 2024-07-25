from django.contrib import admin
from carrito.models import Producto, ItemCarrito, Carrito

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["id","nombre", "descripcion", "precio", "inventario"]
    search_fields = ["nombre", "descripcion", "precio", "inventario"]

admin.site.register(Producto, ProductoAdmin)
admin.site.register(ItemCarrito)
admin.site.register(Carrito)