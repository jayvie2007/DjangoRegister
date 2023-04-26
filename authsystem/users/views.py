from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import User
# Create your views here.

def home(request):
    return render(request,"users/home.html")

def register(request):
    if request.method =='POST':
        first_name = request.POST['first_name']
        middle_name = request.POST['middle_name']
        last_name = request.POST['last_name']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        zip = request.POST['zip']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username):
                messages.info(request, 'Username already exist')
                return redirect(register)
            if User.objects.filter(email=email):
                messages.info(request, 'Email already exist')
                return redirect(register)
            else: 
                new_user = User.objects.create_user(
                    first_name = first_name,
                    middle_name = middle_name,
                    last_name = last_name,
                    address = address,
                    city = city,
                    state = state,
                    zip = zip,
                    email = email,
                    password = password,
                    confirm_password = confirm_password
                )
                new_user.set_password(password)
                new_user.save()
                return redirect('login')


    else:
        return render(request, "users/register.html")
        
def login(request):
    return render(request, "users/login.html")
        