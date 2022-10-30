from django.shortcuts import render

from .models import Productos, CategoriaProd

# Create your views here.

def tienda(request):

    produ=Productos.objects.all()
    return render(request, './Tienda.html', {"produs": produ})

#El ultimo parámetro del render() "{"posteos": posts}" es una forma de llamar a la base de datos.
#Es una Queryset. Al parecer un Queryset es una especie de diccionario con una colección de tods los objetos
#de la base de datos. Y se la llama con un nombre de variable, en este caso "posteos" dos puntos y el nombre 
#de la variable que creamos arriba que contiene todos los objetos osea "post" (posts=Post.objects.all())

def categorias(request, categoria_id):

    categoria2=CategoriaProd.objects.get(id=categoria_id)
    produ=Productos.objects.filter(categorias=categoria2)
    return render(request, "tienda/categoria.html",{'categoria2':categoria2,"produs": produ})
