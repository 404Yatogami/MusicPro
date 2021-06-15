from django.http import response
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from .forms import CustomUserForms, ProductForm, ModifyProductForm
from django.shortcuts import render, redirect
from .models import Categoria, Producto, Sub_Categoria
from django.views.decorators.csrf import csrf_protect
from .cart import Cart
#webpay
import random
from transbank.webpay.webpay_plus.transaction import Transaction
from transbank.error.transbank_error import TransbankError

# Create your views here.

def index(request):
    all_products = Producto.objects.all()
    all_categorias = Categoria.objects.all()

    data={
        'all_categorias' : all_categorias,
        'all_products' : all_products
    }
    return render(request, 'core/index.html', data)

def register(request):
    
    data = {
        'form':CustomUserForms()
    }
    if request.method == 'POST':
        form = CustomUserForms(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            
            return redirect(to='index')

    return render(request, 'core/register.html', data)

def new_product(request):
    data = {
        'form' : ProductForm
    }
    if request.method == 'POST':
        formulario = ProductForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado Correctamente"
        else:
            data["form"] = formulario
    return render(request, 'core/new_product.html', data)

def modify_product(request, id):
    producto = Producto.objects.get(id=id)
    data= {
        'form' : ModifyProductForm(instance = producto),
    }

    if request.method == 'POST' : 
        formulario = ModifyProductForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Modificado Correctamente"
        data['form'] = ModifyProductForm(instance=Producto.objects.get(id=id))

    return render(request, 'core/modify_product.html', data)

def list_product(request):
    product = Producto.objects.all()
    all_categorias = Categoria.objects.all()

    data ={
        'product':product,
        'all_categorias' : all_categorias
    }
    return render(request, 'core/list_product.html', data)

def delete_product(request, id):

    producto = Producto.objects.get(id = id)
    producto.delete()

    return redirect(to="list_product")

def products_cat(request, id):
    all_categorias = Categoria.objects.all()
    subcategoria = Sub_Categoria.objects.get(id=id)
    all_products = Producto.objects.all()
    data = {
        
        'all_products' : all_products,
        'subcategoria' : subcategoria,
        'all_categorias' : all_categorias,
    }
    return render(request, 'core/products_categories.html', data)
def sub_categories(request, id):
    all_categorias = Categoria.objects.all() 
    categoria = Categoria.objects.get(id=id)
    all_subcat = Sub_Categoria.objects.all()
    data = {
        'all_categorias' : all_categorias,
        'categoria' : categoria,
        'all_subcat' : all_subcat,
    }
    return render(request, 'core/sub_categories.html', data)

#Carrito de compras
def cart(request):
    all_categorias = Categoria.objects.all()
    cart = Cart(request)
    total = 0
    FprecioC = 0
    buy_order = str(1)
    session_id = str(1)
    return_url = 'http://127.0.0.1:8000/commit.html'
    for key, value in request.session['cart'].items():
            total = total + (float(value['price']) * value['quantity'])
            # FprecioC=(f'{total:.3f}')
            FprecioC= int(total)
    amount = FprecioC
    try:
        response = Transaction().create(buy_order, session_id, amount, return_url)
        print(amount)
        return render(request, 'core/cart.html', {"response":response, 'all_categorias' : all_categorias})
    except TransbankError as e:
        print(e.message)
        return render(request, 'core/cart.html', {'all_categorias' : all_categorias})

def webpay_plus_commit(request):
    cart = Cart(request)
    token = request.POST.get("token_ws")
    print("commit for token_ws: {}".format(token))

    response = Transaction.commit(token=token)
    print("response: {}".format(response))

    data = {
        'token' : token,
        'response' : response
    }
    return render(request, 'core/commit.html', data)

@csrf_protect
def add_product_catalogo(request, product_id):
    cart = Cart(request)
    product = Producto.objects.get(id=product_id)
    cart.add(product=product)
    return redirect('/')

def add_product_detail(request, product_id):
    cart = Cart(request)
    product = Producto.objects.get(id=product_id)
    cart.add(product=product)
    return redirect(to='index')


def add_product_carrito(request, product_id):
    cart = Cart(request)
    product = Producto.objects.get(id=product_id)
    cart.add(product=product)
    return redirect('/')


@csrf_protect
def decrement_product(request, product_id):
    cart = Cart(request)
    product = Producto.objects.get(id=product_id)
    cart.decrement(product=product)
    return redirect('/core/cart.html')

@csrf_protect
def remove_product(request, product_id):
    cart = Cart(request)
    product = Producto.objects.get(id=product_id)
    cart.remove(product)
    return redirect(to='cart')

@csrf_protect
def clear_cart(request):
    cart = Cart(request)
    cart.clear()
    return redirect('/core/cart.html')