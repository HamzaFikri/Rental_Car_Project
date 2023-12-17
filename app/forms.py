from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from .models import User, Booking, Car, Category
from django import forms



class CustomUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2', 'placeholder':'Enter username'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2', 'placeholder':'Enter email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2', 'placeholder':'Enter password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2', 'placeholder':'Confirm password'}))
    class Meta:
        model = User
        fields =['username', 'email', 'password1', 'password2']

class DateInput(forms.DateInput):
    input_type = 'date'

class BookingCarForm(forms.ModelForm):
    category = forms.Select(attrs={'class': 'form-control'})
    customer_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # start_date = forms.DateField(widget=forms.SelectDateWidget(attrs={'class': ''}))
    # end_date = DateInput()

    class Meta:
        model = Booking
        fields = [ 'category', 'customer_name', 'start_date', 'end_date']
        widgets = {
            'end_date': DateInput(),
            'start_date': DateInput(),
        }
        


class AddCarForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2'}))
    model = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2'}))
    year = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control my-2'}))
    rental_price_per_day = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control my-2'})),
    # available = forms.BooleanField(widget=forms.BooleanField(attrs={'class':'form-control my-2'}))
    # category = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2'}))
    car_image = forms.FileInput(attrs={'class':'form-control'}),

    class Meta:
        model = Car
        fields =['name', 'model', 'year', 'car_image' ,'rental_price_per_day','available','category']


class AddUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2', 'placeholder':'Enter username'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2', 'placeholder':'Enter email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2', 'placeholder':'Enter password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2', 'placeholder':'Confirm password'}))
    class Meta:
        model = User
        fields =['username', 'email', 'password1', 'password2', 'is_staff']