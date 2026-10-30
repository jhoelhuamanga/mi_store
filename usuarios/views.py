from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib.auth import login
from .form import LoginForm

class Autenticacion(FormView):
    template_name = 'usuarios/login.html'
    form_class = LoginForm
    
    # Redirige directamente a la lista de productos al iniciar sesión
    success_url = reverse_lazy('listar_productos')

    def form_valid(self, form):
        user = form.get_user()
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            return self.form_invalid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)