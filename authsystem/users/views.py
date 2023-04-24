from django.shortcuts import render
from django.contrib.auth.models import User, auth
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
    else:
        return render(request, "register.html")
        # if password == confirm_password:
        #     if User.objects.filter(username=username):
        