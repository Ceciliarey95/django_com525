from django.urls import path

from .views import AgregarCategoria, AgregarLibro, ActualizarLibro, EliminarLibro, ListarLibros, listar_libros_por_categoria, ordenar_libros_por, leer_libro


app_name = 'apps.libros'

urlpatterns = [
    path("agregar_categoria/", AgregarCategoria.as_view(), name="agregar_categoria"),
    path("agregar_libro/", AgregarLibro.as_view(), name="agregar_libro"),
    path("actualizar_libro/<int:pk>", ActualizarLibro.as_view(), name="actualizar_libro"),
    path("eliminar_libro/<int:pk>", EliminarLibro.as_view(), name="eliminar_libro" ),
    path("listar_libros/", ListarLibros.as_view(), name="listar_libros"),
    path("listar_por_categoria/<str:categoria>", listar_libros_por_categoria, name='listar_por_categoria'),
    path("ordenar_por", ordenar_libros_por, name='ordenar_por'),
    path("libro/<int:id>", leer_libro, name='libro')
]