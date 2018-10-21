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
            recCar2 = Car.objects.get(id=car3[1].id)
        elif (recCar2.id == car.id):
            recCar3 = Car.objects.get(id=car2[2].id)

    except Car.DoesNotExist:
            raise Http404('Vehicle not found')
    # Pass car history as well
    res = car.history()
    return render(request, 'basesite/car_details.html', {'car': car, 'history': res, 'recCar1': recCar1, 'recCar2': recCar2, 'recCar3': recCar3})

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
    states = Store.objects.values('state').distinct()
    cities = Store.objects.values('city', 'state').distinct()
    car_names = Car.objects.values('name').distinct()
    car_bodys = Car.objects.values('body_type').distinct()
    car_drives = Car.objects.values('drive').distinct()
    #Note sure what this does???????
    form = request.POST # you seem to misinterpret the use of form from django and POST data. you should take a look at [Django with forms][1]
    # you can remove the preview assignment (form =request.POST)
    if request.method == 'POST':
        selected_item = get_object_or_404(Car, pk=request.POST.get('id'))
        # get the user you want (connect for example) in the var "user"
        user.item = selected_item
        user.save()

    # Then, do a redirect for example

    return render(request, 'basesite/recommendation.html', {'states': states, 'cities': cities, 'car_names': car_names, 'car_drives': car_drives, 'car_bodys': car_bodys})
    # Redirects logged in employee to their homepage

def recommended_car(request):
    carID = []
    state = request.GET.get('select_state')
    city =  request.GET.get('select_city')
    store_ids = Store.objects.filter(state=state, city=city)
    print (store_ids[0].city)
    print (store_ids[0].id)
    car_ids = Order.objects.filter(return_store_id=store_ids[0].id)
    for i in car_ids:
        carID.append(i.carID_id)
    print (carID)
    cars = Car.objects.filter(id__in=carID)
    for a in cars:
        print (a.model)
    return render(request, 'basesite/recommended_car.html', {'cars': cars})

# Display customer information and rental history method
def customer(request, id):
    customer = Customer.objects.get(id=id)
    history = Order.objects.filter(customerID=id)
    return render(request, 'basesite/customer.html', {'customer':customer, 'history':history})

