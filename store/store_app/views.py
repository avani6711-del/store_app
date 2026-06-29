from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from django.contrib.auth import authenticate, login
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

def register(request):
    if request.method=="POST":
        customer=CustomerForm(request.POST)
        print(customer)
        if customer.is_valid():
            customer.save()
            print(customer)
            return redirect('/login')
            
        else:
            print("error")
            return HttpResponse("Registration falied ,invalid data")
    else:
        customer=CustomerForm()
    return render(request,'register.html',{"form":customer}) 

def add_product(request):
    if request.method == "POST":
        form = CustomerForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/product')
        else:
            return HttpResponse("invalid form data")
    else:
        form = CustomerForm()    
    return render(request, 'add-product.html',{"form":form})
def loginn(request):
    if request.method=="POST":
        username=request.POST.get('Name')
        password=request.POST.get('Password')

        user=authenticate(request,username=username,Password=password)
        if user is not None:

            login(request,user)
            return redirect('/')
        else:
            return HttpResponse('invalid user or password')
    return render(request,'login.html')