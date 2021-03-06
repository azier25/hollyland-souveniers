from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt

def index(request):
    categories = Category.objects.all()
    if 'customer_id' not in request.session:
        return render(request,'index.html',{'categories':categories})
    else:
        context = {
            "customer_id" : request.session['customer_id'],
            "first_name": request.session['first_name'],
            "last_name": request.session['last_name']
            }
    return render(request,'index.html',{'categories':categories},context)

def signup(request):
    return render(request,'signup.html')


def register(request):
    errors = Customer.objects.register(request.POST)
    if len(errors) > 0:
        for key,error in errors.items():
            messages.error(request, error)
        return redirect(signup)
    else:
        pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        customer = Customer.objects.create(
            email=request.POST['email'].lower(),
            password=pw_hash,
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            country=request.POST['country'],
            address=request.POST['address'],
            postal_code=request.POST['postal_code'],
            phone_number=request.POST['phone_number']
            )
        request.session['customer_id'] = customer.id
        request.session['first_name'] = customer.first_name
        request.session['last_name'] = customer.last_name
        messages.success(request, "Registered successfully :)")
        return redirect(index)


def login(request):
    errors = Customer.objects.login(request.POST)
    if errors:
        for error in errors:
            messages.error(request, error)
        return redirect("/")
    else:
        customer = Customer.objects.filter(email=request.POST['email'].lower())
        if len(customer) < 1:
            messages.error(request, "No customer for that email")
            return redirect("/")
        
        if bcrypt.checkpw(request.POST['password'].encode(), customer[0].password.encode()):
            request.session['customer_id'] = customer[0].id
            request.session['first_name'] = customer[0].first_name
            request.session['last_name'] = customer[0].last_name
            return redirect(index)
        else:
            messages.error(request, "Incorrect Password!")
            return redirect(index)


def logout(request):
    request.session.clear()
    messages.success(request, "Log out successful!")
    return redirect(index)

def items(request,id):
    category = Category.objects.get(id = int(id))
    products = Product.objects.filter(category=category)
    context = {
		'category':category,
		'products':products
	}
    return render(request,'items.html',context)

def cart(request):
    product = Product.objects.all()
    customer_id = request.session['customer_id']
    customer = Customer.objects.get(id = int(customer_id))
    customer_cart = Cart.objects.filter(customer = customer)
    # products = Cart.objects.filter(customer_id = customer.id)
    # total = products.product.price.all.get_total_product_price()
    total = 0
    for total_price in customer_cart:
        price = total_price.quantity * total_price.product.price
        total += price
        # print(total)

    context = {
        'customer_cart':customer_cart,
        'product':product,
        'total':total
        }
    return render(request,'cart.html' ,context)


def addtocart(request,productid):
    product = Product.objects.get(id = productid)
    customer_id = request.session['customer_id']
    customer = Customer.objects.get(id = int(customer_id))
    cart = Cart.objects.create(
        quantity = int(request.POST['quantity']),
        customer = customer,
        product = product,
    )
    return redirect('/cart')

def delete_cart(request, cartid):
    
    cart = Cart.objects.get(id=cartid)
    customer_id = cart.customer
    cart.delete()
    return redirect('/cart')


def order(request):
    # products = Cart.objects.get(id = productid)
    customer_id = request.session['customer_id']
    customer = Customer.objects.get(id = int(customer_id))
    products = Cart.objects.filter(customer_id = customer.id)
    # total = products.product.price.all.get_total_product_price()
    total = 0
    for product in products:
        price = product.quantity * product.product.price
        total += price

    order = Order.objects.create(
        total_price = total,
        customer_id = customer,
        product_id = products.all.id
    )
    return redirect('/cart')

def visa(request):
    return render(request,'last.html')

def demo(request):
    return render(request,'demo.html')



