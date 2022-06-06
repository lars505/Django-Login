import email
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'app/index.html')

def register(request):
    if request.method == 'POST':
        firstname = request.POST['name']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.success(request, 'El usuario ya existe!.')
                return render(request, 'app/register.html')
            elif User.objects.filter(email=email).exists():
                    messages.success(request, 'El correo ya existe!.')
                    return render(request, 'app/register.html')
            else:
                user = User.objects.create_user(username=username, password=password, email=email, first_name=firstname, last_name=lastname)
                user.save()
                messages.success(request, 'Bienvenido!.')
                return render(request, 'app/login.html')
        else:
            return render(request, 'app/register.html')

    return render(request, 'app/register.html')

def login_view(request):
    return render(request, 'app/login.html')

def logout_view(request):
    return render(request, 'app/login.html')
