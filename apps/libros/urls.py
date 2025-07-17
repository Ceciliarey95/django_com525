from django.urls import path

from .views import AgregarCategoria, AgregarLibro, ActualizarLibro, EliminarLibro


app_name = 'apps.libros'

urlpatterns = [
    path("agregar_categoria/", AgregarCategoria.as_view(), name="agregar_categoria"),
    path("agregar_libro/", AgregarLibro.as_view(), name="agregar_libro"),
    path("actualizar_libro/<int:pk>", ActualizarLibro.as_view(), name="actualizar_libro"),
    path("eliminar_libro/", EliminarLibro.as_view(), name="eliminar_libro" )
]

# localhost:8000/libros/agregar_categoria/