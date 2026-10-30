from django.urls import path
from . import views

urlpatterns = [
    path('', views.Autenticacion.as_view(), name='login'),
]