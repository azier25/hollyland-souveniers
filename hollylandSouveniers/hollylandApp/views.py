from django.shortcuts import render
from .models import *

def index(request):
    categories = Category.objects.all()
    return render(request,'index.html',{'categories':categories})

def signup(request):
    return render(request,'signup.html')

def items(request):
    return render(request,'items.html')


