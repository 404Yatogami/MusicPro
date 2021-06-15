from django.urls import path
from core import views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls import include

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
    path('cart.html', views.cart, name='cart' ),
    path('decrement_product/<int:product_id>/', views.decrement_product, name='decrement_product'),
    path('add_product_carrito/<int:product_id>/', views.add_product_carrito, name='add_product_carrito'),
    path('add_product_detail/<int:product_id>/', views.add_product_detail, name='add_product_detail'),
    path('add_product_catalogo/<int:product_id>/', views.add_product_catalogo, name='add_product_catalogo'),
    path('remove_product/<int:product_id>/', views.remove_product, name='remove_product'),
    path('clear/', views.clear_cart, name='clear_cart'),
    path('commit.html', views.webpay_plus_commit, name='webpay_commit' ),
    path('new_product/', views.new_product, name='new_product'),
    path('modify_product/<id>/', views.modify_product, name='modify_product'),
    path('list_product/', views.list_product, name='list_product'),
    path('delete_product/<id>/', views.delete_product, name='delete_product'),
    path('products_cat/<id>/', views.products_cat, name='products_cat'),
    path('sub_categories/<id>/', views.sub_categories, name='sub_categories')
]