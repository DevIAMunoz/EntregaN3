from django.db import models
from django.contrib.auth.models import AbstractUser

class Categoria(models.Model):
    id_categoria = models.AutoField(db_column='idCategoria', primary_key=True)
    categoria = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.categoria)

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=100)
    precio = models.IntegerField(default=0)
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='productos')
    activo = models.BooleanField(default=True)

    def __str__(self):
        return str(self.nombre_producto)
    
    class Meta:
        ordering = ['id_producto']

class CustomUser(AbstractUser):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    rut = models.CharField(max_length=12, unique=True)
    edad = models.PositiveIntegerField()
    estado = models.BooleanField(default=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_groups',  # Cambia a un nombre único
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',  # Cambia a un nombre único
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )

    def __str__(self):
        return self.username

