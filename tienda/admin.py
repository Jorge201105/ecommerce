from django.contrib import admin
from .models import Cliente, Producto, CarritoItem, Pedido, PedidoItem

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    pass  # Aquí puedes personalizar con list_display, search_fields, etc.

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    pass

@admin.register(CarritoItem)
class CarritoItemAdmin(admin.ModelAdmin):
    pass

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    pass

@admin.register(PedidoItem)
class PedidoItemAdmin(admin.ModelAdmin):
    pass
