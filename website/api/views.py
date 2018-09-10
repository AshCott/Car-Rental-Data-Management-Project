from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from basesite.models import Car
from django.views.decorators.csrf import csrf_exempt

# don't want to use a token to access an api
@csrf_exempt
def carByID(request):
    try:
        id = request.POST
        car = Car.objects.get(id=id['id'])

    # failed to find, sends json
    except Car.DoesNotExist:
        return JsonResponse({'car':'Failed to find'})

    return JsonResponse(car.JSonObject())

@csrf_exempt
def search(request):
    print("\n\n SEARCH STARTED \n\n")
    try:
        vals = request.POST
        car = Car.objects.filter(name__icontains=vals['name'])
    except Car.DoesNotExist:
        return JsonResponse({'val': 'failed'})
    # list comprehensions are fun
    resp = {'test': [item.JSonObject() for item in car]}
    return JsonResponse(resp)
