from django.shortcuts import render

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