from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.core.mail import send_mail



##################################################################

from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import Car
from .models import Store
from django.shortcuts import get_object_or_404

from django.contrib.auth.decorators import login_required
from django.contrib import auth




# Create your views here.
def index(request):
    return render(request, 'basesite/home.html') #IMPORTANT NOTE - 'base.html' is
    #automatically found, as django takes all templates from (project)/(app)/templates
    #and considers them the same thing. may make things difficult if we have multiple apps

    # Also for dynamically rendered pages pass a dictionary into render, and
    # this will be used in Jinja templating


def employee_home(request):
    return render(request, 'basesite/employee_home.html')
    # Redirects logged in employee to their homepage



def logout(request):
    auth.logout(request)
    return render(request, 'basesite/logout.html')
    # Redirects a logged out user to the Logout page


################################################33

def email_new_user(sender, **kwargs):
    if kwargs["created"]:  # only for new users
        new_user = kwargs["instance"]
        # send email to new_user.email ..

        subject = 'Welcome: ' + new_user.first_name + ' ' + new_user.last_name + '!'
        message = 'Dear ' + new_user.first_name + ',\n\n' + 'Welcome to Car Rental Company!\n' + 'We are so excited to have you on board.\n' + '\nYour new username is: ' + new_user.username + '\n\nFor security purposes your new password has been encrypted. The character based password you created will not be sent via email for security purposes. Please remember the password that you have been given by the administrator. If it has been forgotten, contact an administrator and they will reset the password for you. \n\nWe are exited to work with you! \n\nRegards,\n\nThe Car Rental Company Admin Team'
        CompanyEmail = 'carrentalcompany299@gmail.com'
        EmployeeEmail = new_user.email
        send_mail(subject, message, CompanyEmail, [EmployeeEmail,],fail_silently=False)

post_save.connect(email_new_user, sender=User)

##########################################################


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
    except Car.DoesNotExist:
            raise Http404('Vehicle not found')
    return render(request, 'basesite/car_details.html', {'car': car})

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
    cities = Store.objects.values('city').distinct()
    car_names = Car.objects.values('name').distinct()
    car_bodys = Car.objects.values('body_type').distinct()
    car_drives = Car.objects.values('drive').distinct()
    print (car_names)
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
