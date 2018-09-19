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
