from django.db import models


class Equities(models.Model):
    equity = models.CharField(max_length=4, primary_key=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    sector1 = models.CharField(max_length=200)
    sector2 = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.equity} , {self.nombre}'

    class Meta:
        ordering = ['equity']  # entrega los datos ordenados alfabéticamente


class Bancos(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nombre}'


class Nis_pos(models.Model):
    equity = models.ForeignKey(Equities, on_delete=models.CASCADE)
    banco = models.ForeignKey(Bancos, on_delete=models.CASCADE)
    fechacompra = models.DateField('fecha compra')
    Cantidad = models.IntegerField()
    precio_compra = models.FloatField()

    def __str__(self):
        return f'{self.equity} {self.Cantidad}'


