from django.db import models

# Create your models here.

from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.json import KeyTransformNumericLookupMixin
from django.db.models.fields.related import ForeignKey

# Create your models here.

class Categoria(models.Model): 
    categoria = models.CharField(max_length=200, null=False)
    def __str__(self):
        return self.categoria

class Sub_Categoria(models.Model):
    nom_subcat = models.CharField(max_length=200, null=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    def __str__(self):
        return self.nom_subcat

class Producto(models.Model):
    serie_producto = models.CharField(null=False, max_length=20)
    marca = models.CharField(max_length=100, null=False)
    codigo = models.CharField(max_length=50, null=False)
    nombre = models.CharField(max_length=200, null=False)
    valor = models.IntegerField(null=False)
    fecha = models.DateTimeField(null=True)
    imagen = models.ImageField(upload_to="instrumentos", null=True)
    sub_categoria = models.ForeignKey(Sub_Categoria, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre