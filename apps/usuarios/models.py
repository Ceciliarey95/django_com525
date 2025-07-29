from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

# Create your models here.

class Usuario(AbstractUser):
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    email = models.EmailField()
    fecha_nacimiento = models.DateField('Fecha_nacimiento', default='2000-1-1')
    es_colaborador = models.BooleanField('Es_colaborador', default=False)
    imagen = models.ImageField(null=True, blank=True, upload_to='usuarios', default='usuarios/usuario_default.png')

    class Meta: 
        ordering = ('-nombre',)

    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return reverse('index')