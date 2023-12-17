from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from app.forms import *

# Create your views here.
def home(request):
    car = Car.objects.all()
    context = {
        'car':car
    }
    return render(request, 'app/index.html',context)

def category(request):
    category = Category.objects.all()
    context = {'category':category}
    return render(request, 'app/category.html', context)

def categoryview(request, id):
    if(Category.objects.filter(id=id)):
        # car = Car.objects.filter(category_id=id, rental_price_per_day__gte = 100)
        # car = Car.objects.filter(category_id=id, available = 1)
        car = Car.objects.filter(category_id=id)
        categ = Category.objects.filter(id=id)[0]
        context = {'category':categ, 'car': car }
        return render(request, "app/car/index.html", context)
    else:
        messages.warning(request, "No such category found")
        return redirect('category')

def carview(request,categ_id, car_id):
    if(Category.objects.filter(id=categ_id)):
        if(Car.objects.filter(id=car_id)):
            car = Car.objects.filter(id=car_id).first
            context = {'car':car}
        else:
            messages.warning(request, "No such Car found")
            return redirect('category')
    else:
        messages.warning(request, "No such category found")
        return redirect('category')
    return render(request, "app/car/view.html", context)



 

    