from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def about(request):
    return render(request, 'about.html')
@login_required
def blog_detail(request):
    return render(request, 'blog-detail.html')
@login_required
def blog(request):
    return render(request, 'blog.html')
@login_required
def contact(request):
    return render(request, 'contact.html')

def home_02(request):
    return render(request, 'home-02.html')

def home_03(request):
    return render(request, 'home-03.html')
@login_required
def product_detail(request):
    return render(request, 'product-detail.html')
@login_required
def product(request):
    return render(request, 'product.html')
@login_required
def shoping_cart(request):
    return render(request, 'shoping-cart.html')
@login_required
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
@login_required
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
        e=request.POST.get('Email')
        pwd=request.POST.get('Password')

        user= CustomerModel.objects.get(email = e)
        if user.email == e and user.password == pwd:
            return redirect('/product')
        else:
            return HttpResponse('invalid user or password')
    return render(request,'login.html')
