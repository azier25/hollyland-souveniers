from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def signup(request):
    return render(request,'signup.html')

def items(request):
    return render(request,'items.html')


def login(request):
    if request.method == 'POST':
        Email_address = request.POST['Email_address']
        Password = request.POST['Password']

        user = user.authenticate(Email)
        address = Email
        address, Password = Password)
        if user is not None:
            user.login(request, user)
            return redirect('/')
        else:
            massages.info(request, 'invalid credentials')
            return (redirect('login')
                    else:
        return render(request, 'login.html)


def home(request):
    return render(request, "index.html")

def register(request):
    errors = Customer.objects.register(request.POST)
    if len(errors) > 0:
        for key,error in errors.items():
            messages.error(request, error)
        return redirect("/")
    else:
        pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        user = User.objects.create(email=request.POST['email'].lower(), password=pw_hash, first_name=request.POST['first_name'], last_name=request.POST['last_name'],birthday=request.POST['birthday'])
        request.session['user_id'] = user.id
        request.session['first_name'] = user.first_name
        messages.success(request, "Registered successfully :)")
        return redirect("/success")
