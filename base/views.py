from django.shortcuts import render
from .models import *
from .forms import OrderForm
from django.http import JsonResponse
import json
import datetime
from . utils import cookieCart

# Create your views here.

products = [
    {'id': 1, 'name': 'BubbleTea 1', 'images':'https://images.pexels.com/photos/4013151/pexels-photo-4013151.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2', 'prix': '12.99$'},
    {'id': 2, 'name': 'BubbleTea 2', 'images':'https://images.pexels.com/photos/4013151/pexels-photo-4013151.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2', 'prix': '6.99$'},
    {'id': 3, 'name': 'BubbleTea 3', 'images':'https://images.pexels.com/photos/4013151/pexels-photo-4013151.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2', 'prix': '3.99$'},
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

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        
    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'base/store.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'base/checkout.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'base/cart.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('productId:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order = order, product=product)

    if action =='add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe= False)

def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == order.get_cart_total:
            order.complete = True
        order.save()

        if order.shipping == True:
            ShippingAddress.objects.create(
                customer = customer,
                order = order,
                address = data['shipping']['address'],
                city = data['shipping']['city'],
                country = data['shipping']['country'],
                zipcode = data['shipping']['zipcode'],
            )

    else:
        print('User is not logged in..')
    return JsonResponse('Payment complete!', safe= False)