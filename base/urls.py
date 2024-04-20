from django.urls import path
from . import views
from django.urls import path

urlpatterns = [
    path('', views.store, name='store'),
    path('login/', views.login, name ="login"),
    #path('login/', views.LoginView.as_view(), name="login"),
    path('register/', views.register, name="register"),
    path('profile/', views.profile, name="profile"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('store/', views.store, name="store"),
    
    

    path('orderView', views.viewOrder, name="viewOrder"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
    path('register_form', views.registerForm, name="register_form")
]
