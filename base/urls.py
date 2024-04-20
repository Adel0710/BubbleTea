from django.urls import path
from . import views
from django.urls import path
from .views import MyTokenObtainPairView, Home

urlpatterns = [
    path("token/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('', Home.as_view()),
    path('login/', views.login, name="login"),
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
