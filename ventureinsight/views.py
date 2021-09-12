from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


# Create your views here.
def base(request):
    return render(request, 'base.html')  

def signup(request):
    if request.method == "POST":
        try:
            User.objects.get(username = request.POST['username'])
            return render (request,'accounts/signup.html', {'error':'Username is already taken!'})
        except User.DoesNotExist:
            user = User.objects.create_user(request.POST['email'],password=request.POST['password'])
            auth.login(request,user)
            return redirect('home')
    else:
        return render(request, 'signup.html')  

def login(request):
    if request.method == "POST":
        user = auth.authenticate(username=request.POST['email'],password = request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render (request,'login.html', {'error':'Username or password is incorrect!'})
    else:
        return render(request, 'login.html') 
     

def dashboard(request):
    return render(request, 'dashboard.html')  

def companyinfo(request):
    return render(request, 'companyinfo.html')  

def profile(request):
    return render(request, 'profile.html')  

def home(request):
    return render(request, 'home.html') 