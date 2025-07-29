from django.db import models

from apps.libros.models import Libro
from apps.usuarios.models import Usuario

# Create your models here.
class Opinion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    texto = models.TextField(verbose_name='Opinion')
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.texto
    
    class Meta:
        ordering = ['-fecha',]