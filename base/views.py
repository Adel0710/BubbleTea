from django.shortcuts import render
from .models import *
from .forms import OrderForm
from dja

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

def order(request, pk):
    order = None
    for i in orders:
        if i['id'] == int(pk):
            order = i
    context = {'order': order}
    return render(request, 'base/order.html', context)

def viewOrder(request):
    form = OrderForm()
    context = {'form': form}
    return render(request, 'base/order_form.html', context)

def store(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'base/store.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        #Create empty cart for non-logged users
        order = {'get_cart_total':0, 'get_cart_items':0}
        items = []

    context = {'items': items, 'order': order}
    return render(request, 'base/checkout.html', context)

def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items':0}

    context = {'items': items, 'order': order}
    return render(request, 'base/cart.html', context)