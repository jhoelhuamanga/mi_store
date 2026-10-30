from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Producto
from .form import ProductoForm # Ojo: recuerda que tu archivo se llama form.py (sin 's')

class ProductoListView(LoginRequiredMixin, ListView):
    model = Producto
    template_name = 'productos/index.html'
    context_object_name = 'productos'
    login_url = 'login'

class ProductoCreateView(LoginRequiredMixin, CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'productos/crear.html'
    success_url = reverse_lazy('listar_productos')
    login_url = 'login'

class ProductoUpdateView(LoginRequiredMixin, UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'productos/editar.html'
    success_url = reverse_lazy('listar_productos')
    login_url = 'login'

class ProductoDeleteView(LoginRequiredMixin, DeleteView):
    model = Producto
    template_name = 'productos/eliminar.html'
    success_url = reverse_lazy('listar_productos')
    login_url = 'login'