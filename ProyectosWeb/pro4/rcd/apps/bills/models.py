from django.db import models

# Create your models here.
class Docuemnts(models.Model):
    type = models.CharField('Tipo', max_length=20, unique=True)


    class Meta():
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'
        ordering = ('id',)
        

    def __str__(self):
        return f'{self.type}'


class Workers(models.Model):
    name = models.CharField('Nombre', max_length=20)
    surname = models.CharField('Apellido', max_length=20)
    position = models.CharField('Cargo', max_length=30)


    class Meta():
        verbose_name = 'Trabajador'
        verbose_name_plural = 'Trabajadores'
        ordering = ('id',)
      

    def __str__(self):
        return f'{self.name}'


class Tickets(models.Model):
    user = models.ForeignKey(Workers, on_delete=models.CASCADE, verbose_name='Usuario')
    type = models.ForeignKey(Docuemnts, on_delete=models.DO_NOTHING, verbose_name='Tipo')
    date = models.DateField('Fecha')
    rut = models.CharField('Rut', max_length=10)
    name = models.CharField('Nombre local', max_length=30)
    use = models.CharField('Uso', max_length=100)
    cash = models.PositiveIntegerField('Valor')
    image = models.ImageField('Imagen', upload_to='tickets')


    class Meta():
        verbose_name = 'Boleta'
        verbose_name_plural = 'Boletas'
        ordering = ('date',)


    def __str__(self):
        return f'{self.id} - {self.name}'


class Bills(models.Model):
    user = models.ForeignKey(Workers, on_delete=models.CASCADE, verbose_name='Usuario')
    type = models.ForeignKey(Docuemnts, on_delete=models.DO_NOTHING, verbose_name='Tipo')
    date = models.DateField('Fecha')
    rut = models.CharField('Rut', max_length=10)
    name = models.CharField('Nombre local', max_length=30)
    address = models.CharField('Dirección', max_length=100)
    giro = models.CharField('Giro', max_length=30)
    use = models.CharField('Uso', max_length=100)
    neto = models.PositiveIntegerField('Neto')
    iva = models.PositiveIntegerField('Iva')
    total = models.PositiveIntegerField('Total')
    image = models.ImageField('Imagen', upload_to='bills')


    class Meta():
        verbose_name = 'Factura'
        verbose_name_plural = 'Facturas'
        ordering = ('date',)


    def __str__(self):
        return f'{self.id} - {self.name}'