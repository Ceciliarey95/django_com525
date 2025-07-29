from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from apps.opiniones.models import Opinion
from apps.opiniones.forms import OpinionForm

from .models import Categoria, Libro

# Create your views here.

# ----- Categoria ------

class AgregarCategoria(CreateView):
    model = Categoria
    fields= ['nombre']
    template_name = 'libros/agregar_categoria.html'
    success_url = reverse_lazy('index')

class ActualizarCategoria(UpdateView):
    pass

class EliminarCategoria(DeleteView):
    pass

# ---- LIBROS -----

class AgregarLibro(CreateView):
    model = Libro
    fields= ['titulo', 'autor', 'categoria', 'descripcion', 'imagen']
    template_name = 'libros/agregar_libro.html'
    success_url = reverse_lazy('index')

class ActualizarLibro(UpdateView):
    model = Libro
    fields= ['titulo', 'autor', 'categoria', 'descripcion', 'imagen']
    template_name = 'libros/agregar_libro.html'
    success_url = reverse_lazy('index')

class EliminarLibro(DeleteView):
    model = Libro
    template_name = "genericos/confirma_eliminar.html"
    success_url = reverse_lazy('index')

class ListarLibros(ListView):
    model = Libro
    template_name = 'libros/listar_libros.html'
    context_object_name = "libros"
    paginate_by = 3

    def get_context_data(self):
        context = super().get_context_data()
        categorias = Categoria.objects.all()
        context['categorias'] = categorias
        return context
    
    def get_queryset(self):
        query = self.request.GET.get('buscador')
        queryset = super().get_queryset()

        if query:
            queryset = queryset.filter(titulo__icontains=query)
        
        return queryset.order_by('titulo')
    
def listar_libros_por_categoria(request, categoria):
    categoria_filtrada = Categoria.objects.filter(nombre = categoria)
    libros = Libro.objects.filter(categoria=categoria_filtrada[0].id).order_by('fecha_agregado')
    categorias = Categoria.objects.all()
    template_name = 'libros/listar_libros.html'
    context ={
        'libros': libros,
        'categorias': categorias
    }
    return render(request, template_name, context)

def ordenar_libros_por(request):
    orden = request.GET.get('orden', '')

    if orden == 'fecha':
        libros = Libro.objects.order_by('fecha_agregado')
    elif orden == 'titulo':
        libros = Libro.objects.order_by('titulo')
    else:
        libros = Libro.objects.all()

    context = {
        'libros' : libros
    }
    return render(request, 'libros/listar_libros.html', context)

def leer_libro(request, id):
    libro = Libro.objects.get(id = id)
    opiniones = Opinion.objects.filter(libro=id)
    form = OpinionForm(request.POST)
    
    if form.is_valid():
        if request.user.is_authenticated:
            aux = form.save(commit=False)
            aux.libro = libro
            aux.usuario = request.user
            aux.save()
            form = OpinionForm()
        else:
            return redirect('apps.usuarios:iniciar_sesion')
    context={
        'libro' : libro,
        'form' : form,
        'opiniones' : opiniones
    }
    return render(request, 'libros/libro.html', context)