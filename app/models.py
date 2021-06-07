from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields.related import ForeignKey
from django.utils import timezone

# Create your models here.


class Usuarios(AbstractUser):
    first_name = models.CharField(name='nombre', max_length=40)
    rut = models.CharField(max_length=45)
    is_trabajador = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = "Usuarios"


class Vehiculos(models.Model):
    marca = models.CharField(max_length=45)
    modelo = models.CharField(max_length=45)
    year = models.IntegerField()
    precio_dia = models.IntegerField()
    kilometrahe = models.IntegerField()
    estado = models.CharField(max_length=45)
    usuario_id = ForeignKey(Usuarios, on_delete=models.CASCADE)

    def __str__(self):
        return self.marca + "--" + self.modelo + "-->" + str(self.id)

    class Meta:
        verbose_name_plural = "Vehiculos"


class Arriendos(models.Model):
    observaciones = models.TextField(max_length=65000)
    precio = models.IntegerField(blank=True, null=True)
    fecha_inicio = models.DateTimeField(default=timezone.now)
    fecha_termino = models.DateTimeField(blank=True, null=True)
    usuario_id = ForeignKey(Usuarios, on_delete=models.CASCADE)
    vehiculo_id = ForeignKey(Vehiculos, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):

        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Arriendos, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.usuario_id) + '--' + str(self.vehiculo_id)

    class Meta:
        verbose_name_plural = "Arriendos"


class Extras(models.Model):
    nombre = models.CharField(max_length=45)
    vehiculo_id = ForeignKey(Vehiculos, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.vehiculo_id) + "--" + self.nombre

    class Meta:
        verbose_name_plural = "Extras"
