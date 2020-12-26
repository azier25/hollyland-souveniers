from django.urls import path
from . import views

urlpatterns = [
    path('',views.index , name= 'index'),
    path('signup/',views.signup),
    path('register',views.register),
    path('login/',views.login),
    path('logout/', views.logout),
    path('items/<int:id>',views.items),
    path('cart/',views.cart),
    path('addtocart/<int:productid>',views.addtocart),
    path('delete/<int:cartid>/', views.delete_cart),
    path('order/',views.order),

]