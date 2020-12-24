from django.urls import path
from . import views

urlpatterns = [
    path('',views.index , name= 'index'),
    path('signup/',views.signup),
    path('items/',views.items),
    path('login/',views.login),
]