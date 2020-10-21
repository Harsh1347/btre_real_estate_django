from django.shortcuts import render,redirect

def register(request):
    return render(request,'accounts/register.html')

def login(request):
    return render(request,'accounts/login.html')

def dashboard(request):
    return render('index')

def logout(request):
    return redirect(request,'accounts/login.html')