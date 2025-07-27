from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Producto, CarritoItem, Cliente, Pedido, PedidoItem
from .forms import RegistroUsuarioForm
from django.contrib.auth import login

def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'tienda/registro.html', {'form': form})

@login_required
def home(request):
    return render(request, 'tienda/home.html')

@login_required
def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'tienda/lista_productos.html', {'productos': productos})

@login_required
def agregar_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    cliente = Cliente.objects.get(user=request.user)
    cantidad = int(request.POST['cantidad'])

    item, creado = CarritoItem.objects.get_or_create(cliente=cliente, producto=producto)
    if not creado:
        item.cantidad += cantidad
    else:
        item.cantidad = cantidad
    item.save()

    return redirect('ver_carrito')

@login_required
def ver_carrito(request):
    cliente = Cliente.objects.get(user=request.user)
    items = CarritoItem.objects.filter(cliente=cliente)
    total = sum([item.subtotal() for item in items])
    return render(request, 'tienda/ver_carrito.html', {'items': items, 'total': total})

@login_required
def finalizar_pedido(request):
    cliente = Cliente.objects.get(user=request.user)
    items = CarritoItem.objects.filter(cliente=cliente)
    total = sum([item.subtotal() for item in items])

    pedido = Pedido.objects.create(cliente=cliente, total=total)

    for item in items:
        PedidoItem.objects.create(
            pedido=pedido,
            producto=item.producto,
            cantidad=item.cantidad
        )
        item.delete()

    return render(request, 'tienda/pedido_exito.html', {'pedido': pedido})
