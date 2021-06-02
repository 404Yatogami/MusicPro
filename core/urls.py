from django.urls import path
from core import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='core/login.html'), name='login'),
    path('cart.html', views.cart, name='cart' ),
    path('decrement_product/<int:product_id>/', views.decrement_product, name='decrement_product'),
    path('add_product_carrito/<int:product_id>/', views.add_product_carrito, name='add_product_carrito'),
    path('add_product_detail/<int:product_id>/', views.add_product_detail, name='add_product_detail'),
    path('add_product_catalogo/<int:product_id>/', views.add_product_catalogo, name='add_product_catalogo'),
    path('remove_product/<int:product_id>/', views.remove_product, name='remove_product'),
    path('clear/', views.clear_cart, name='clear_cart'),
    path('commit.html', views.webpay_plus_commit, name='webpay_commit' ),
    path('new_instrument/', views.new_instrument, name='new_instrument'),
]