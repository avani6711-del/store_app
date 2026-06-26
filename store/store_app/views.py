from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def about(request):
    return render(request, 'about.html')

def blog_detail(request):
    return render(request, 'blog-detail.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')

def home_02(request):
    return render(request, 'home-02.html')

def home_03(request):
    return render(request, 'home-03.html')

def product_detail(request):
    return render(request, 'product-detail.html')

def product(request):
    return render(request, 'product.html')

def shoping_cart(request):
    return render(request, 'shoping-cart.html')

def index(request):
    return render(request, 'index.html')