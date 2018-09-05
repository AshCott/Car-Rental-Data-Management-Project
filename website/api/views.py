from django.shortcuts import render
from django.http import JsonResponse

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
