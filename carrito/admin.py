from django.contrib import admin
from carrito.models import Producto, ItemCarrito, Carrito, Customer

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["id","nombre", "descripcion", "precio", "inventario"]
    search_fields = ["nombre", "descripcion", "precio", "inventario"]

class ItemCarritoAdmin(admin.ModelAdmin):
    list_display = ["id"]

class CustomerAdmin(admin.ModelAdmin):
    list_display = ["id","first_name", "last_name"]

admin.site.register(Producto, ProductoAdmin)
admin.site.register(ItemCarrito, ItemCarritoAdmin)
admin.site.register(Carrito)
admin.site.register(Customer)