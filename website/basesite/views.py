from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.core.mail import send_mail

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.http import Http404
from .models import Car
from .models import Store
from .models import Order
from .models import Customer

import random

from django.shortcuts import get_object_or_404

from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.template import RequestContext
from django.conf.urls import handler404, handler500
from django.shortcuts import render_to_response
from django.template import RequestContext



# Create your views here.
def index(request):
    return render(request, 'basesite/home.html') #IMPORTANT NOTE - 'base.html' is
    #automatically found, as django takes all templates from (project)/(app)/templates
    #and considers them the same thing. may make things difficult if we have multiple apps

    # Also for dynamically rendered pages pass a dictionary into render, and
    # this will be used in Jinja templating

def error_404_view(request, exception):
    data = {"name": "boi"}
    return render(request,'basesite/404.html', data)

def error_500_view(request, exception):
    data = {"name": "boi"}
    return render(request,'basesite/500.html', data)



def employee_home(request):
    return render(request, 'basesite/employee_home.html')
    # Redirects logged in employee to their homepage


def logout(request):
    auth.logout(request)
    return render(request, 'basesite/logout.html')
    # Redirects a logged out user to the Logout page


def email_new_user(sender, **kwargs):
    if kwargs["created"]:  # only for new users
        new_user = kwargs["instance"] # new_user variable contains currently submitted information
        # create email strings
        subject = 'Welcome: ' + new_user.first_name + ' ' + new_user.last_name + '!'
        message = 'Dear ' + new_user.first_name + ',\n\n' + 'Welcome to Car Rental Company!\n' + 'We are so excited to have you on board.\n' + '\nYour new username is: ' + new_user.username + '\n\nFor security purposes your new password has been encrypted. The character based password you created will not be sent via email for security purposes. Please remember the password that you have been given by the administrator. If it has been forgotten, contact an administrator and they will reset the password for you. \n\nRegards,\n\nThe Car Rental Company Admin Team'
        CompanyEmail = 'carrentalcompany299@gmail.com' # Company Email, defined by the SMTP host
        EmployeeEmail = new_user.email # Extract entered user email
        # send email to supplied email using send_mail function ..
        send_mail(subject, message, CompanyEmail, [EmployeeEmail,],fail_silently=False)

# Use the post_save signal to execute the above function
# when the save button is pressed on the register form
post_save.connect(email_new_user, sender=User)


def search(request):
    sample = {'cars': [
    {'name': 'Toyota', 'type': 'Sedan', 'speed': 'Slow'},
    {'name': 'Ferarri', 'type': 'Racecar', 'speed': 'Fast'}
    ]
    }
    # note that each car in the cars list cannot be named. no dictionary of named dictionaries
    # also, 'cars' must refer to a list/array, not a dict

    return render(request, 'basesite/search.html', sample)

def customer(request):
    return render(request, 'basesite/customer.html')
    # View Customers page

def car_details(request, id):
    try:
        car = Car.objects.get(id=id)
        car2 = Car.objects.filter(drive = car.drive).order_by('?')
        car3 = Car.objects.filter(body_type = car.body_type).order_by('?')
        car4 = Car.objects.filter(seating_capacity = car.seating_capacity).order_by('?')

        recCar1 = Car.objects.get(id=car2[0].id)
        recCar2 = Car.objects.get(id=car3[0].id)
        recCar3 = Car.objects.get(id=car4[0].id)

        if recCar1.id == car.id:
            recCar1 = Car.objects.get(id=car2[1].id)
        elif (recCar2.id == car.id):
            recCar2 = Car.objects.get(id=car2[1].id)
        elif (recCar2.id == car.id):
            recCar3 = Car.objects.get(id=car2[2].id)

    except Car.DoesNotExist:
            raise Http404('Vehicle not found')
    # Pass car history as well
    res = car.history()
    return render(request, 'basesite/car_details.html', {'car': car, 'history': res, 'recCar1': recCar1, 'recCar2': recCar2, 'recCar3': recCar3})

def customer_details(request, id):
    try:
        customer = Customer.objects.get(id=id)
        history = Order.objects.filter(customerID=id)
    except Customer.DoesNotExist:
            raise Http404('Vehicle not found')
    return render(request, 'basesite/customer_details.html', {'customer':customer, 'history':history})

def car_history(request):
    return render(request, 'basesite/carhistory.html')

def car_percentage(request):
    sample = {'uniqueCars': [
    {'name': 'Alfa Romeo', 'perc': '1.75'},
    {'name': 'Audi', 'perc': '5.59'},
    {'name': 'BMW', 'perc': '17.48'},
    {'name': 'Chrysler', 'perc': '4.90'},
    {'name': 'Datson', 'perc': '0.70'},
    {'name': 'Eunos', 'perc': '0.70'},
    {'name': 'Honda', 'perc': '0.35'},
    {'name': 'Land Rover', 'perc': '2.80'},
    {'name': 'Mazda', 'perc': '13.64'},
    {'name': 'Mercedes-Benz', 'perc': '1049'},
    {'name': 'Mitsubishi', 'perc': '0.35'},
    {'name': 'Nissan', 'perc': '2.80'},
    {'name': 'Renault', 'perc': '6.99'},
    {'name': 'Saab', 'perc': '6.99'},
    {'name': 'Toyota', 'perc': '0.70'},
    {'name': 'Volkswagen', 'perc': '15.03'},
    {'name': 'Volvo', 'perc': '6.64'},
    ]
    }

def recommendation(request):
    # Pull data required for dropdowns from database
    states = Store.objects.values('state').distinct()
    cities = Store.objects.values('city', 'state').distinct().order_by('city')
    car_names = Car.objects.values('name').distinct().order_by('name').order_by('name')
    car_bodys = Car.objects.values('body_type').distinct().order_by('body_type')
    car_drives = Car.objects.values('drive').distinct().order_by('drive')
    car_model = Car.objects.values('model').distinct().order_by('model')
    car_year = Car.objects.values('year').distinct().order_by('-year')
    car_seating_capacity = Car.objects.values('seating_capacity').distinct().order_by('seating_capacity')

    # pass the data and render webpage
    return render(request, 'basesite/recommendation.html', {'states': states, 'cities': cities, 'car_names': car_names, 'car_drives': car_drives, 'car_bodys': car_bodys, 'car_model': car_model, 'car_year': car_year, 'car_seating_capacity': car_seating_capacity})


def recommended_car(request):
    # Get user input from dropdown selections
    carID = []
    city =  request.GET.get('select_city')
    car_brand = request.GET.get('select_car_brand')
    car_body = request.GET.get('select_car_body')
    car_drive = request.GET.get('select_car_drive')
    car_model = request.GET.get('select_car_model')
    car_year = request.GET.get('select_car_year')
    car_seating_capacity = request.GET.get('select_car_seating_capacity')

    # Query database for required data
    store_ids = Store.objects.filter(city=city)
    car_ids = Order.objects.filter(return_store_id=store_ids[0].id)

    # Filter data based upon user selections
    for i in car_ids:
        carID.append(i.carID_id)
    cars = Car.objects.filter(id__in=carID)
    if car_brand != "":
        cars = cars.filter(name=car_brand)
    if car_body != "":
        cars = cars.filter(body_type=car_body)
    if car_drive != "":
        cars = cars.filter(drive=car_drive)
    if car_model != "":
        cars = cars.filter(model=car_model)
    if car_year != "":
        cars = cars.filter(year=car_year)
    if car_seating_capacity != "":
        cars = cars.filter(seating_capacity=car_seating_capacity)
    
    # Select a random car to be recommended or alert the webpage that their is no results found
    if len(cars) != 0:
        reco_car = cars[random.randint(0, len(cars)-1)]
        print (reco_car)
        return render(request, 'basesite/recommended_car.html', {'cars': cars, 'car_drive':car_drive, 'reco_car':reco_car})
    else:
        no_results = True
        return render(request, 'basesite/recommended_car.html', {'no_results':no_results})


def stores(request):
    stores = Store.objects.all()
    return render(request, 'basesite/stores.html',{'stores': stores})

def store(request, id):
    store = Store.objects.get(id=id)
    # Have to get all cars, then filter on html page
    currentCars = Car.objects.all()
    return render(request, 'basesite/store.html', {'store': store, 'cars': currentCars})
