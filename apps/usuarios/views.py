from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django. contrib import messages

from .models import Usuario
from .forms import RegistroUsuarioForm

# Create your views here.

class RegistroUsuario(CreateView):
    model = Usuario
    form_class = RegistroUsuarioForm
    template_name = 'usuarios/registrar.html'
    success_url = reverse_lazy('index')

def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    template_name = 'usuarios/listar_usuarios.html'
    context = {
        'usuarios' : usuarios
    }
    return render(request, template_name, context)

class ActualizarUsuario(LoginRequiredMixin, UpdateView):
    model = Usuario
    fields = ['nombre', 'apellido', 'email', 'fecha_nacimiento', 'imagen']
    template_name = 'usuarios/registrar.html'
    success_url = reverse_lazy('index')

    def dispatch(self, request, *args, **kwargs):
        user_id = self.kwargs.get('pk')
        if str(user_id) != str(request.user.pk):
            return Http404("No tienes permiso para actualizar este usuario")
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        messages.success(self.request, "Perfil actualizado correctamente")
        return super().form_valid(form)
    