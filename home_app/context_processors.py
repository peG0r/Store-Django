from carrito_app.models import Carrito

def carrito_context(request):
    carrito = None
    if request.user.is_authenticated:
        carrito = Carrito.objects.filter(usuario=request.user).first()
    return {
        'carrito': carrito,
    }
