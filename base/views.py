from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

rooms = [
    {'id': 1, 'name': 'dashboard'},
    {'id': 2, 'name': 'shop'}
    
]

def home(request):
    context = {'rooms':rooms}
    return render(request, 'base/home.html', context)

def dashboard(request):
    return render(request, 'dashboard.html')

def shop(request):
    return render(request, 'shop.html')

def admin(request):
    return render(request , 'admin.html')

def room (request,pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
            context = {'room': room}
    return render(request, 'base/room.html')

def createOrder(request):
    return render(request)
