from django.shortcuts import render
from django.contrib.auth import login, authenticate
from .forms import CustomUserForms, ProductForm
from django.shortcuts import render, redirect
from .models import Categoria, Producto
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

def new_instrument(request):
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
    return render(request, 'core/new_instrument.html', data)
    #Carrito de compras
def cart(request):
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
        return render(request, 'core/cart.html', {"response":response})
    except TransbankError as e:
        print(e.message)
        return render(request, 'core/cart.html', {})

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