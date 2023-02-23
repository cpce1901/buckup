from django.db import models
from apps.author.models import Autor

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField('nombre', max_length=30)

    def __str__(self):
        return f'{self.nombre}'


class Libro(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    autores = models.ManyToManyField(Autor)
    titulo = models.CharField('nombre', max_length=50)
    fecha = models.DateField('fecha de lanzamiento')
    portada = models.ImageField(upload_to='portada')
    visitas = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.titulo}'