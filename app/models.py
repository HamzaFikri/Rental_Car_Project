from django.db import models
import datetime, os
from django.contrib.auth.models import User

# Create your models here.
def get_file_path(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (nowTime, original_filename)
    return os.path.join('uploads/', filename)

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=get_file_path, blank=True, null=True)

    def __str__(self):
        return self.name

class Car(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    rental_price_per_day = models.FloatField()
    available = models.SmallIntegerField(default=0)
    car_image = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.model} - {self.year}"


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    customer_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
