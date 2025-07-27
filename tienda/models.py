from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)

    def __str__(self):
        return self.nombre

class CarritoItem(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.producto.precio * self.cantidad

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre} de {self.cliente.user.username}"

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(
        max_length=20,
        choices=[
            ('pendiente', 'Pendiente'),
            ('procesando', 'Procesando'),
            ('enviado', 'Enviado'),
            ('entregado', 'Entregado'),
        ],
        default='pendiente'
    )

    def __str__(self):
        return f"Pedido #{self.id} - {self.cliente.user.username}"

class PedidoItem(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    def subtotal(self):
        return self.producto.precio * self.cantidad

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre} (Pedido #{self.pedido.id})"
