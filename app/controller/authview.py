from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from app.forms import CustomUserForm

def register(request):
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration Successfully! Login To Continue")
            return redirect('/login')
    context = {'form':form}
    return render(request, "app/auth/register.html", context)

def loginpage(request):
    if request.user.is_authenticated:
        messages.warning(request, "You are already logged in")
        return redirect('/')
    else:
        if request.method == 'POST':
            name = request.POST.get('username')
            passwd = request.POST.get('password')

            user = authenticate(request, username=name, password=passwd)

            if user is not None:
                login(request, user)
                messages.success(request, "Logged Successfully")
                return redirect('/')
            else:
                messages.error(request, "Invalid Username or Password")
                return redirect('/login')
    return render(request, "app/auth/login.html")

def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Logged out Successfully")
    return redirect('/')