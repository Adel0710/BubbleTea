from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('profile/', views.profile, name="profile"),
    path('order/<str:pk>', views.order, name="order"),
    path ('insertregister/', views.insertregister, name= "insertregister")
]

