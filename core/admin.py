from django.contrib import admin
from .models import Categoria, Producto, Sub_Categoria

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Sub_Categoria)
admin.site.register(Producto)

