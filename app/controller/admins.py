from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib import messages
from django.http import JsonResponse
from app.models import *
from app.forms import *
from django.conf import settings
from django.contrib.auth.decorators import login_required

def dashboard(request):
    car = Car.objects.all()
    context = {
        'car':car
    }
    return render(request, 'app/admin-panel/dashboard.html', context)

def addcar(request):
    if request.method == 'POST':
        car = Car.objects.all()
        form = AddCarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            print("-----------------"+form.errors)
    else:
        form = AddCarForm()
    return render(request, 'app/admin-panel/addcar.html', {'form': form})

def deletecar(request,id):
        if request.method == 'POST':
            pi = Car.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/admin-panel')

def adduser(request):
    form = AddUserForm()
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration Successfully! Login To Continue")
            return redirect('viewuser')
    context = {'form':form}
    return render(request, "app/admin-panel/adduser.html", context)


def viewuser(request):
    user = User.objects.all()
    return render(request, 'app/admin-panel/viewuser.html',{'user': user})

def deleteuser(request,id):
        if request.method == 'POST':
            pi = User.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/viewuser')
        
def bookview(request):
    book = Booking.objects.all()
    context = {
        'book':book
    }
    return render(request, 'app/admin-panel/bookview.html', context)

