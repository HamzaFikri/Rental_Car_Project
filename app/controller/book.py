from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from app.models import *
from app.forms import BookingCarForm
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.db.models.expressions import RawSQL
from django.db.models.query import QuerySet
from datetime import datetime, timedelta

def addtobook(request):
    if request.method == "POST":
        form = BookingCarForm(request.POST, request.FILES)
        if request.POST.get('bookCar'):
            cars = Car.objects.filter(category_id =request.POST.get('category'))
            # end_date = datetime.strptime(request.POST.get('end_date'), '%Y-%m-%d')+ timedelta(days=1)
            # request.POST.get("end_date",end_date)
            # print("=========================================================")
            # print(end_date)
            # # request.POST.set('end_date', end_date)
            # form.initial["end_date"] = end_date
            # print("=========================================================")
            # post = request.POST
            # post.update({"end_date":end_date})
            # print(post)
            return render(request, 'app/PrecarsCheckBox.html', {'form': form, 'cars': cars})

# ===========================================
        

        
        if request.POST.get('CheckAvailibality'):
            # allcars = Car.objects.filter(category_id =request.POST.get('category'))
            # cars = Car.objects.filter(category_id =False)
            # print("1=====================")
            # print(allcars)
            # for car in allcars:
            #     bks = Booking.objects.filter(car_id = car.id, start_date__gte = request.POST.get('start_date'), end_date__lte = request.POST.get('end_date')).count()
            #     if car.available > bks:
            #         cars |= Car.objects.filter(id = car.id)
                
            # print("2=====================")
            # print(cars)


            

            # def getDays(tempbk):
            #     tempbk = Booking.objects.filter(category_id =request.POST.get('category'))[2]
            #     delta = tempbk.end_date - tempbk.start_date   # returns timedelta
            #     for i in range(delta.days):
            #         day = tempbk.start_date + timedelta(days=i)
                    
            # print(day)
            # return 0


            allcars = Car.objects.filter(category_id =request.POST.get('category'))
            # cars = Car.objects.filter(category_id =False)
            
            excludedCarIds = []
            end_date = datetime.strptime(request.POST.get('end_date'), '%Y-%m-%d')
            start_date = datetime.strptime(request.POST.get('start_date'), '%Y-%m-%d')
            dff = end_date - start_date
            for car in allcars:
                for i in range(dff.days):
                    day = start_date + timedelta(days=i)
                    
                    bks = Booking.objects.filter(car_id = car.id, start_date__lte = day, end_date__gt = day).count()
                    if bks >= car.available:
                        excludedCarIds.append(car.id)
                        break
            cars = Car.objects.filter(category_id =request.POST.get('category')).exclude(id__in = excludedCarIds)
           
            # for item in cars:
            # cars = Car.objects.filter(RawSQL("SELECT * FROM app_car WHERE category_id = %s and available >(SELECT COUNT(app_booking.id) FROM app_booking ,app_car WHERE app_car.id=app_booking.car_id and start_date = '%s' and end_date = '%s')",[request.POST.get('category'),request.POST.get('start_date'),request.POST.get('end_date')]))
            
            # cars = QuerySet.annotate(val=RawSQL("SELECT * FROM app_car WHERE category_id = %s and available >(SELECT COUNT(app_booking.id) FROM app_booking ,app_car WHERE app_car.id=app_booking.car_id and start_date = '%s' and end_date = '%s')",[request.POST.get('category'),request.POST.get('start_date'),request.POST.get('end_date')]))
            # cars = Car.objects.filter(id__in=RawSQL("SELECT id FROM app_car WHERE category_id = %s ",[request.POST.get('category')]))
            
            return render(request, 'app/carsCheckBox.html', {'form': form, 'cars': cars})
        if request.POST.get('BookNow'):
            book = Booking()
            categid = request.POST.get('category')
            categ= Category.objects.filter(id=int(categid))[0]
            book.category = categ

            carid = request.POST.get('car')
            cars= Car.objects.filter(id=int(carid))[0]
            book.car = cars

            userid = request.POST.get('user_id')
            users= User.objects.filter(id=int(userid))[0]
            book.user = users
            
            book.customer_name = request.POST.get('customer_name')
            book.start_date = request.POST.get('start_date')
            book.end_date = request.POST.get('end_date')
            # book.startdate = request.POST.get('start-date',None)
            # book.enddate = request.POST.get('end-date',None)
            # print(book)
            # return 0
            book.save()
            # return redirect('/')
    else:
        form = BookingCarForm()
    return render(request, 'app/booking.html', {'form': form})
    # return render(request, 'app/booking.html')