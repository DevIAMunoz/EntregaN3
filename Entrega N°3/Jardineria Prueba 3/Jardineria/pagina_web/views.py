from django.shortcuts import render, redirect, get_object_or_404
from .models import Categoria, Producto
from django.contrib.auth import login, authenticate, logout
from .forms import UsuarioForm
from django.contrib import messages
from django.contrib.auth.models import User
from .decorators import admin_only

def index(request):
    context = {}
    return render(request, 'pagina/index.html', context)

def Fertilizantes(request):
    fertilizantes = Categoria.objects.get(categoria='Fertilizantes')
    productos_fertilizantes = Producto.objects.filter(id_categoria=fertilizantes)
    return render(request, 'pagina/Fertilizantes.html', {'productos': productos_fertilizantes})

def Herramientas(request):
    herramientas = Categoria.objects.get(categoria='Herramientas')
    productos_herramientas = Producto.objects.filter(id_categoria=herramientas)
    return render(request, 'pagina/Herramientas.html', {'productos': productos_herramientas})

def Maceteros(request):
    maceteros = Categoria.objects.get(categoria='Maceteros')
    productos_maceteros = Producto.objects.filter(id_categoria=maceteros)
    return render(request, 'pagina/Maceteros.html', {'productos': productos_maceteros})

def Semillas(request):
    semillas = Categoria.objects.get(categoria='Semillas')
    productos_semillas = Producto.objects.filter(id_categoria=semillas)
    return render(request, 'pagina/Semillas.html', {'productos': productos_semillas})

def admin(request):
    productos = Producto.objects.all()
    context = {"productos": productos}
    return render(request, 'pagina/admin.html', context)

@admin_only
def crud(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, 'pagina/admin_list.html', context)

@admin_only
def productosAdd(request):
    if request.method == "POST":
        # Obtener datos del formulario
        id_producto = request.POST["id_producto"]
        nombre_producto = request.POST["nombre_producto"]
        precio = request.POST["precio"]
        id_categoria = request.POST["categoria"]

        # Obtener objeto de categoría
        objCategoria = Categoria.objects.get(id_categoria=id_categoria)

        # Crear objeto Producto
        nuevo_producto = Producto(
            id_producto=id_producto,
            nombre_producto=nombre_producto,
            precio=precio,
            id_categoria=objCategoria,
            activo=True
        )

        # Manejar la carga de la imagen
        if 'foto' in request.FILES:
            nuevo_producto.foto = request.FILES['foto']

        nuevo_producto.save()

        # Obtener productos y categorías para el contexto
        productos = Producto.objects.all()
        categorias = Categoria.objects.all()
        context = {
            'mensaje': "¡Producto Añadido!",
            'productos': productos,
            'categorias': categorias
        }
        return render(request, 'pagina/admin_add.html', context)
    
    else:
        # Si no es método POST, mostrar el formulario vacío
        productos = Producto.objects.all()
        categorias = Categoria.objects.all()
        context = {
            'productos': productos,
            'categorias': categorias
        }
        return render(request, 'pagina/admin_add.html', context)

@admin_only
def productos_del(request, pk):
    context = {}
    try:
        producto = Producto.objects.get(id_producto=pk)
        producto.delete()
        mensaje = "¡Producto Eliminado!"
        productos = Producto.objects.all()
        context = {'productos': productos, 'mensaje': mensaje}
        return render(request, 'pagina/admin_list.html', context)
    except Producto.DoesNotExist:
        mensaje = "¡Error! Producto no existe"
        productos = Producto.objects.all()
        context = {'productos': productos, 'mensaje': mensaje}
        return render(request, 'pagina/admin_list.html', context)

@admin_only    
def productos_findEdit(request, pk):
    if pk != "":
        try:
            producto = Producto.objects.get(id_producto=pk)
            categorias = Categoria.objects.all()
            context = {'producto': producto, 'categorias': categorias}
            return render(request, 'pagina/admin_edit.html', context)
        except Producto.DoesNotExist:
            context = {'mensaje': "¡Error! Producto no existe"}
            return render(request, 'pagina/admin_list.html', context)

@admin_only        
def productosUpdate(request):
    if request.method == "POST":
        id_producto = request.POST.get("id_producto")
        nombre_producto = request.POST.get("nombre_producto")
        precio = request.POST.get("precio")
        id_categoria = request.POST.get("categoria")
        nueva_foto = request.FILES.get("nueva_foto")

        print(f"id_producto: {id_producto}")
        print(f"nombre_producto: {nombre_producto}")
        print(f"precio: {precio}")
        print(f"id_categoria: {id_categoria}")
        print(f"nueva_foto: {nueva_foto}")

        if None in [id_producto, nombre_producto, precio, id_categoria]:
            categorias = Categoria.objects.all()
            productos = Producto.objects.all()
            context = {
                'mensaje': "¡Error! Faltan datos en el formulario.",
                'categorias': categorias,
                'productos': productos
            }
            return render(request, 'pagina/admin_list.html', context)

        objCategoria = Categoria.objects.get(id_categoria=id_categoria)

        producto = Producto.objects.get(id_producto=id_producto)
        producto.nombre_producto = nombre_producto
        producto.precio = precio
        producto.id_categoria = objCategoria

        if nueva_foto:
            producto.foto = nueva_foto
        
        producto.save()

        categorias = Categoria.objects.all()
        context = {
            'mensaje': "¡Producto Actualizado!",
            'categorias': categorias,
            'producto': producto
        }
        return render(request, 'pagina/admin_edit.html', context)
    else:
        productos = Producto.objects.all()
        context = {'productos': productos}
        return render(request, 'pagina/admin_list.html', context)


def registro(request):
    # Your registration logic here
    return render(request, 'pagina/registro.html')



def registro_usuario(request):
    if request.method == 'POST':
        # Procesar el formulario enviado
        username = request.POST.get('username')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        email = request.POST.get('email')
        rut = request.POST.get('rut')
        password = request.POST.get('password')
        edad = request.POST.get('edad')

        # Aquí puedes crear el usuario en tu base de datos
        user = User.objects.create_user(username=username, email=email, password=password, first_name=nombre, last_name=apellido)
        user.save()

        # Envía un mensaje de éxito
        messages.success(request, '¡Registro exitoso! Ahora puedes iniciar sesión.')

        # Redirige a alguna página o vistal
        return redirect('index')

    # Si no es un método POST, renderiza el formulario
    return render(request, 'pagina/registro.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('crud')  # Redirige a la página principal después del login exitoso
        else:
            # Manejar caso de login fallido
            return render(request, 'pagina/index.html', {'error': 'Usuario o contraseña incorrectos'})

    return render(request, 'tu_template_login.html')

def logout_view(request):
    logout(request)
    # Puedes redirigir a donde quieras después de cerrar sesión
    return redirect('index')

def forbidden_view(request):
    return render(request, 'forbidden.html')
