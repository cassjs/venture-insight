from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from ventureinsight.scraper import VentureData

VentureData()
print("")

def signup(request):
    if request.method == "POST":
        try:
            User.objects.get(username = request.POST['email'])
            return render (request,'signup.html', {'error':'Username is already taken!'})
        except User.DoesNotExist:
            user = User.objects.create_user(request.POST['email'],password=request.POST['password'])
            auth.login(request,user)
            return redirect('/login')
    else:
        return render(request, 'signup.html')  

def login(request):
    if request.method == "POST":
        user = auth.authenticate(username=request.POST['email'],password = request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('/dashboard')
        else:
            return render (request,'login.html', {'error':'Username or password is incorrect!'})
    else:
        return render(request, 'login.html') 
     

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html') 
    else :
        return redirect('/login')

def companyinfo(request):
    if request.user.is_authenticated:
        return render(request, 'companyinfo.html')  
    else :
        return redirect('/login')

def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html', {'user' : request.user})  
    else :
        return redirect('/login')

def home(request):
    return render(request, 'home.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

    