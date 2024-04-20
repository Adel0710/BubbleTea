from django.shortcuts import render
from .models import *
from .forms import OrderForm
from django.http import JsonResponse
import json
import datetime
from . utils import cookieCart, cartData, guestOrder
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = response.data["access"]
        response.set_cookie("Tapioca_pearl", token, httponly=True)
        return response


class Home(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


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

def registerForm(request):
    print()
    # if request.method == 'POST':
    #     query = Customer.objects.raw("INSERT INTO users(lastname, firstname, email, password) VALUES ('%s','%s','%s','%s')")
    #     print(query)

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

    data = cartData(request)
    cartItems = data['cartItems']

    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'base/store.html', context)

def checkout(request):
    
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'base/checkout.html', context)

def cart(request):

    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

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

    else:
        customer, order = guestOrder(request, data)

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

    return JsonResponse('Payment complete!', safe= False)