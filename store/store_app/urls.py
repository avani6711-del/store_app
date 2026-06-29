from django.urls import path
from .views import *

urlpatterns = [
    path('about/', about, name='about'),
    path('blog-detail/', blog_detail, name='blog-detail'),
    path('blog/', blog, name='blog'),
    path('contact/', contact, name='contact'),
    path('', home_02, name='home-02'),
    path('home-03/', home_03, name='home-03'),
    path('index/', index, name='index'),
    path('product-detail/', product_detail, name='product-detail'),
    path('product/', product, name='product'),
    path('shopping-cart/', shoping_cart, name='shoping_cart'),
    path('register/',register,name='register'),
    path('add-product/', add_product,name='add-product'),
    path('login/',login,name='login'),
]