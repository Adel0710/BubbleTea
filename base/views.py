from django.shortcuts import render
from django.db import connection
from .models import Register


# Create your views here.

products = [
    {'id': 1, 'name': 'BubbleTea 1'},
    {'id': 2, 'name': 'BubbleTea 2'},
    {'id': 3, 'name': 'BubbleTea 3'},
]

orders = [
    {'id': 1, 'name': 'Order 1'},
    {'id': 2, 'name': 'Order 2'},
    {'id': 3, 'name': 'Order 3'},
]

def home(request):
    context = {'products': products}
    return render(request, 'base/home.html', context)

def login(request):
    return render(request, 'base/login.html')

def register(request):
    return render(request, 'base/register.html')

def profile(request):
    context = {'orders': orders}
    return render(request,'base/profile.html', context)

def userreg(request):
    return render(request, "base/userreg.html")
    

def order(request, pk):
    order = None
    for i in orders:
        if i['id'] == int(pk):
            order = i
    context = {'order': order}
    return render(request, 'base/order.html', context)



def insertregister(request):
    vuid = request.POST("id");
    vunom = request.POST("firstName");
    vuprenom = request.POST("lastName")
    vuemail = request.POST("email");
    vuusername = request.POST("username");
    vupassword = request.POST("password");
    us = Register(id = vuid, nom = vunom, prenom = vuprenom, email = vuemail, username = vuusername, password = vupassword);
    
    
    return render(request, 'base/register.html',{})



