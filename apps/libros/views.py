from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

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

