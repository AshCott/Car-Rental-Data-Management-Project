from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from basesite.models import Car
from django.views.decorators.csrf import csrf_exempt

# This is an incredibly basic JsonResponse, which is what the api will return
def sample(request):
    return JsonResponse({'Message':
    'This is a sample api query response'})

def sampleCar(request):
    car = {'cars': [
    {'name': 'Mazda', 'type': 'Small', 'speed': 'Slow'},
    {'name': 'Bus', 'type': 'Trap', 'speed': 'Nonexistent'}
    ]
    }
    return JsonResponse(car)

# don't want to use a token to access an api
@csrf_exempt
def carByID(request):
    try:
        id = request.POST
        # apparently request object is a generator so i need to call next to get the value
        car = Car.objects.get(id=next(id.values()))
    except Car.DoesNotExist:
        return({'car':'Failed to find'})

    return JsonResponse(car.JSonObject())
