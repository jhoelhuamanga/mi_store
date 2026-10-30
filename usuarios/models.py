from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UsuarioManager(BaseUserManager):
    def create_user(self, username, nombres, cedula, email, password=None):
        if not email:
            raise ValueError('El usuario debe tener un correo electrónico')
        
        usuario = self.model(
            username=username.strip(),
            nombres=nombres,
            cedula=cedula,
            email=self.normalize_email(email),
        )
        usuario.set_password(password)
        usuario.save()
        return usuario

    def create_superuser(self, username, nombres, cedula, email, password):
        usuario = self.create_user(
            username,
            nombres,
            cedula,
            email,
            password
        )
        usuario.is_admin = True
        usuario.save()
        return usuario

class Usuarios(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True)
    nombres = models.CharField(max_length=100)
    cedula = models.CharField(max_length=10)
    email = models.EmailField(max_length=250, unique=True)
    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['nombres', 'cedula', 'email']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin