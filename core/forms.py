
from django.forms.fields import ChoiceField
from django.forms.widgets import Select
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from core.models import Producto


class CustomUserForms(UserCreationForm):

    email = forms.EmailField()
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)
    username = forms.CharField(label='Nombre de usuario')
    #Clase para agregar mas campos, la cantidad de campos y sus nombres se puede ver en ADMIN
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')
        help_texts = {k:"" for k in fields}
    
class ProductForm(ModelForm):
    serie_producto = forms.CharField(label='Serie del Producto')
    marca = forms.CharField(label='Marca')
    codigo = forms.CharField(label='Codigo')
    nombre = forms.CharField(label='Nombre')
    valor = forms.IntegerField(label='Valor')
    class Meta:
        model = Producto
        fields = ['serie_producto', 'marca', 'codigo', 'nombre', 'valor', 'sub_categoria', 'imagen']
        help_texts = {k:"" for k in fields}

class ModifyProductForm(ModelForm):
    marca = forms.CharField(label='Marca')
    codigo = forms.CharField(label='Codigo')
    nombre = forms.CharField(label='Nombre')
    valor = forms.IntegerField(label='Valor')
    class Meta:
        model = Producto
        fields = ['marca', 'codigo', 'nombre', 'valor', 'sub_categoria', 'imagen']
        help_texts = {k:"" for k in fields}