from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/ ', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('profile/', views.profile, name="profile"),
    path('order/<str:pk>', views.order, name="order"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('store/', views.store, name="store"),
    

    path('orderView', views.viewOrder, name="viewOrder")
]
