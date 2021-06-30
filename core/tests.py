from django.http import request
from django.test import TestCase
from . import views
from .models import Categoria, Producto, Sub_Categoria
# Create your tests here.

class TestViews(TestCase):

    def setUp(self):
        Categoria.objects.create(categoria = "Instrumentos de Viento")
        Categoria.objects.create(categoria = "Instrumentos de Percusion")
        Sub_Categoria.objects.create(nom_subcat="Saxofon", categoria_id="1")
        Sub_Categoria.objects.create(nom_subcat="Bateria Electrica", categoria_id="2")
        Producto.objects.create(serie_producto="SF901", marca="Martin", codigo="Martin901", nombre="Martin Saxofon Premium Edition", valor="469990", sub_categoria_id="1")
        Producto.objects.create(serie_producto="SF983", marca="Saxo", codigo="Saxo983", nombre="Saxofon Nuevo Sellado", valor="100000", sub_categoria_id="1")
        

    def test_add_categoria(self):
        result = Categoria.objects.get(categoria = "Instrumentos de Viento")
        self.assertEqual(result.categoria, "Instrumentos de Viento")
    
    def test_add_subcat(self):
        result = Sub_Categoria.objects.get(nom_subcat="Saxofon")
        self.assertEqual(result.nom_subcat, "Saxofon")
    
    def test_add_product(self):
        result = Producto.objects.get(serie_producto="SF901")
        self.assertEqual(result.serie_producto, "SF901")

    def test_mod_product(self):
        Producto.objects.filter(serie_producto="SF983").update(valor="250000")
        result = Producto.objects.get(serie_producto="SF983")
        print(f"Producto {result.serie_producto} Modificado correctamente con valor de {result.valor}")
        self.assertEqual(result.valor, 250000)
    
    def test_mod_category(self):
        Categoria.objects.filter(id="2").update(categoria="Percusion")
        result = Categoria.objects.get(id="2")
        print(f"Categoria {result.id} modificada correctamente con nombre {result.categoria}")
        self.assertEqual(result.categoria, "Percusion")

    def test_mod_subcat(self):
        Sub_Categoria.objects.filter(id="2").update(nom_subcat="Bateria Electronica")
        result = Sub_Categoria.objects.get(id="2")
        print(f"Categoria {result.id} modificada correctamente con nombre {result.nom_subcat}")
        self.assertEqual(result.nom_subcat, "Bateria Electronica")
    
    def test_delete_product(self):
        if Producto.objects.get(serie_producto="SF983"):
            Producto.objects.get(serie_producto="SF983").delete()
            print("Producto eliminado correctamente")
    
    def test_delete_subcat(self):
        if Sub_Categoria.objects.get(id="2"):
            Sub_Categoria.objects.get(id="2").delete()
            print("SubCategoria eliminada correctamente")

    def test_delete_category(self):
        if Categoria.objects.get(id="2"):
            Categoria.objects.get(id="2").delete()
            print("Categoria eliminada correctamente")
    
    