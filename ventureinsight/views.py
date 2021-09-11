from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request, 'base.html')  

def signup(request):
    return render(request, 'signup.html')  

def login(request):
    return render(request, 'login.html')  

def dashboard(request):
    return render(request, 'dashboard.html')  

def companyinfo(request):
    return render(request, 'companyinfo.html')  

def profile(request):
    return render(request, 'profile.html')  

def home(request):
    return render(request, 'home.html') 